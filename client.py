"""
Ocular Choroidal Vascularity Index (CVI) & Subfoveal Choroidal Thickness Client.
Zero-mock pure Python standard library implementation.
Calculates Choroidal Vascularity Index (CVI = LA / TCA * 100), Subfoveal Choroidal Thickness (SFCT),
Luminal-to-Stromal Area Ratio, and Pachychoroid vs Chorioretinal Atrophy Classification.
"""

import math
from typing import Dict, Any, Optional


class ChoroidalVascularityIndexClient:
    """
    Evaluates choroidal microvascular architecture and thickness via binarized EDI / SS-OCT:
    - SFCT (um): subfoveal choroidal thickness from RPE to sclerochoroidal interface
    - TCA (mm2): Total Choroidal Area
    - LA (mm2): Luminal Area (vascular lumen volume)
    - SA (mm2): Stromal Area = TCA - LA
    - CVI (%) = (LA / TCA) * 100
    - L/S ratio = LA / SA
    """

    def __init__(self):
        pass

    def evaluate_cvi(
        self,
        subfoveal_choroidal_thickness_um: float,
        total_choroidal_area_mm2: float,
        luminal_area_mm2: float,
        patient_age_years: Optional[int] = 40,
        axial_length_mm: Optional[float] = 24.0,
        eye_examined: Optional[str] = "OD"
    ) -> Dict[str, Any]:
        """
        Calculates CVI and choroidal morphological metrics.
        subfoveal_choroidal_thickness_um: SFCT in micrometers (e.g. 280.0 um).
        total_choroidal_area_mm2: binarized TCA in square millimeters (e.g. 1.25 mm2).
        luminal_area_mm2: binarized vascular luminal area in square millimeters (e.g. 0.82 mm2).
        """
        if subfoveal_choroidal_thickness_um <= 0 or total_choroidal_area_mm2 <= 0 or luminal_area_mm2 <= 0:
            raise ValueError("Thickness and area parameters must be strictly positive.")
        if luminal_area_mm2 >= total_choroidal_area_mm2:
            raise ValueError("Luminal area must be smaller than total choroidal area.")

        # Stromal area (SA in mm2)
        stromal_area_mm2 = total_choroidal_area_mm2 - luminal_area_mm2

        # Choroidal Vascularity Index (CVI in %)
        cvi_pct = (luminal_area_mm2 / total_choroidal_area_mm2) * 100.0

        # Luminal to Stromal Ratio
        ls_ratio = luminal_area_mm2 / stromal_area_mm2 if stromal_area_mm2 > 0 else 0.0

        # Age-adjusted expected normal SFCT (~300 um at 30yo, thinning ~15 um per decade)
        expected_sfct = 320.0 - (patient_age_years - 20) * 1.5

        # Clinical Classification (Pachychoroid vs Healthy vs Chorioretinal Atrophy):
        # Normal reference (Agrawal et al. consensus):
        # CVI: 64.0% to 68.5%
        # SFCT: 220 to 350 um (in emmetropic adults)
        # Pachychoroid Spectrum:
        # CVI > 70.0% and/or SFCT > 360 um (hyperpermeable dilated Haller pachyvessels)
        # Choroidal Thinning / Ischemic Atrophy:
        # CVI < 60.0% and/or SFCT < 150 um (high myopia / dry AMD choriocapillaris loss)
        if cvi_pct > 70.0 or subfoveal_choroidal_thickness_um > 370.0:
            choroidal_state = "Pachychoroid Spectrum (Hypervascular / Dilated Pachyvessels)"
            clinical_risk = "Elevated hydrostatic pressure in Haller layer vessels; investigate for Central Serous Chorioretinopathy (CSCR) or pachychoroid neovasculopathy."
        elif cvi_pct < 60.0 or subfoveal_choroidal_thickness_um < 150.0:
            choroidal_state = "Choroidal Vascular Atrophy / Ischemic Rarefaction"
            clinical_risk = "Attenuated choroidal perfusion; associated with age-related macular degeneration (AMD), myopic choroidal thinning, or vascular occlusion."
        elif cvi_pct >= 63.5 and cvi_pct <= 69.0:
            choroidal_state = "Normal Physiological Choroidal Vascularity"
            clinical_risk = "Equilibrated vascular luminal volume and interstitial stroma sustaining normal photoreceptor and RPE metabolic demand."
        else:
            choroidal_state = "Intermediate / Borderline Choroidal Architecture"
            clinical_risk = "Mild divergence in vascular-to-stromal proportion; monitor with longitudinal serial OCT scans."

        return {
            "status": "success",
            "choroidal_metrics": {
                "subfoveal_thickness_sfct_um": round(subfoveal_choroidal_thickness_um, 1),
                "expected_age_adjusted_sfct_um": round(expected_sfct, 1),
                "choroidal_vascularity_index_cvi_pct": round(cvi_pct, 2),
                "luminal_to_stromal_ratio": round(ls_ratio, 2),
                "total_area_tca_mm2": round(total_choroidal_area_mm2, 3),
                "luminal_area_la_mm2": round(luminal_area_mm2, 3),
                "stromal_area_sa_mm2": round(stromal_area_mm2, 3)
            },
            "patient_context": {
                "patient_age_years": patient_age_years,
                "axial_length_mm": axial_length_mm,
                "eye_examined": eye_examined
            },
            "clinical_diagnosis": {
                "choroidal_state": choroidal_state,
                "clinical_pathophysiology": clinical_risk
            }
        }
