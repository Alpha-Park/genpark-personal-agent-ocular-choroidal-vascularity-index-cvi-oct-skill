"""
MCP Server for Ocular Choroidal Vascularity Index (CVI) & Subfoveal Choroidal Thickness.
Exposes tools for EDI/SS-OCT choroidal vascularity and pachychoroid vs atrophy staging.
"""

import json
from typing import Dict, Any, Optional
from client import ChoroidalVascularityIndexClient


def handle_evaluate_cvi(params: Dict[str, Any]) -> Dict[str, Any]:
    subfoveal_choroidal_thickness_um = float(params.get("subfoveal_choroidal_thickness_um", 280.0))
    total_choroidal_area_mm2 = float(params.get("total_choroidal_area_mm2", 1.25))
    luminal_area_mm2 = float(params.get("luminal_area_mm2", 0.82))
    patient_age_years = int(params.get("patient_age_years", 40))
    axial_length_mm = float(params.get("axial_length_mm", 24.0))
    eye_examined = str(params.get("eye_examined", "OD"))

    client = ChoroidalVascularityIndexClient()
    return client.evaluate_cvi(
        subfoveal_choroidal_thickness_um=subfoveal_choroidal_thickness_um,
        total_choroidal_area_mm2=total_choroidal_area_mm2,
        luminal_area_mm2=luminal_area_mm2,
        patient_age_years=patient_age_years,
        axial_length_mm=axial_length_mm,
        eye_examined=eye_examined
    )


TOOLS = {
    "evaluate_cvi": {
        "description": "Calculates EDI/SS-OCT Choroidal Vascularity Index (CVI = LA/TCA * 100), Subfoveal Choroidal Thickness (SFCT), and pachychoroid vs choroidal atrophy classification.",
        "parameters": {
            "type": "object",
            "properties": {
                "subfoveal_choroidal_thickness_um": {
                    "type": "number",
                    "description": "Subfoveal choroidal thickness in micrometers (e.g. 280.0 um)."
                },
                "total_choroidal_area_mm2": {
                    "type": "number",
                    "description": "Total binarized choroidal area in mm2 (e.g. 1.25 mm2)."
                },
                "luminal_area_mm2": {
                    "type": "number",
                    "description": "Luminal vascular area in mm2 (e.g. 0.82 mm2)."
                },
                "patient_age_years": {
                    "type": "integer",
                    "description": "Patient age in years, default 40."
                },
                "axial_length_mm": {
                    "type": "number",
                    "description": "Ocular axial length in mm, default 24.0."
                },
                "eye_examined": {
                    "type": "string",
                    "description": "Eye tested ('OD' or 'OS'), default 'OD'."
                }
            },
            "required": ["subfoveal_choroidal_thickness_um", "total_choroidal_area_mm2", "luminal_area_mm2"]
        },
        "handler": handle_evaluate_cvi
    }
}


def process_request(request_str: str) -> str:
    try:
        req = json.loads(request_str)
        method = req.get("method")
        req_id = req.get("id")

        if method == "tools/list":
            tools_list = [
                {
                    "name": name,
                    "description": spec["description"],
                    "inputSchema": spec["parameters"]
                }
                for name, spec in TOOLS.items()
            ]
            return json.dumps({"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools_list}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            if tool_name not in TOOLS:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}
                })

            result = TOOLS[tool_name]["handler"](args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }
            })

        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32600, "message": f"Unsupported method '{method}'"}
            })

    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        if line.strip():
            print(process_request(line))
            sys.stdout.flush()
