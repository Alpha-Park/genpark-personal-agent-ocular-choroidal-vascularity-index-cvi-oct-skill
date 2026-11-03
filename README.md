# Ocular Choroidal Vascularity Index (CVI) & Subfoveal Choroidal Thickness Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-green.svg)](https://modelcontextprotocol.io/)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](requirements.txt)
[![Status: Production-Ready](https://img.shields.io/badge/status-production--ready-success.svg)](https://github.com/alphaparkinc)

A zero-dependency, mathematically rigorous personal agent skill that evaluates choroidal vascular luminal proportions and subfoveal thickness via binarized Enhanced Depth Imaging Optical Coherence Tomography (EDI-OCT).

## Architecture

```mermaid
flowchart TD
    A[EDI / SS-OCT Cross-Sectional Scan] --> B[Segment RPE and Sclerochoroidal Interface]
    B --> C[Measure Subfoveal Choroidal Thickness SFCT]
    C --> D[Binarize into Luminal Area LA & Stromal Area SA]
    D --> E[Compute CVI = LA / Total Area * 100 & L/S Ratio]
    E --> F[Pachychoroid vs Atrophy vs Normal Stratification]
```

## Quick Start

```python
from client import ChoroidalVascularityIndexClient

client = ChoroidalVascularityIndexClient()
result = client.evaluate_cvi(
    subfoveal_choroidal_thickness_um=280.0,
    total_choroidal_area_mm2=1.25,
    luminal_area_mm2=0.82,
    patient_age_years=40
)
print("CVI (%):", result["choroidal_metrics"]["choroidal_vascularity_index_cvi_pct"])
print("Diagnosis:", result["clinical_diagnosis"]["choroidal_state"])
```

## License
Apache-2.0
