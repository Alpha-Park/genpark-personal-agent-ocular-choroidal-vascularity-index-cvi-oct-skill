"""
Example usage of Ocular Choroidal Vascularity Index (CVI) & Subfoveal Choroidal Thickness.
Demonstrates normal physiological choroid vs pachychoroid spectrum (CSCR).
"""

from client import ChoroidalVascularityIndexClient

def main():
    client = ChoroidalVascularityIndexClient()

    print("=== Case 1: Healthy Physiological Choroidal Architecture ===")
    normal_case = client.evaluate_cvi(
        subfoveal_choroidal_thickness_um=285.0,
        total_choroidal_area_mm2=1.35,
        luminal_area_mm2=0.89,
        patient_age_years=35,
        axial_length_mm=23.8,
        eye_examined="OD"
    )
    print("Choroidal Morphology:")
    print(f"  SFCT:        {normal_case['choroidal_metrics']['subfoveal_thickness_sfct_um']} um")
    print(f"  CVI:         {normal_case['choroidal_metrics']['choroidal_vascularity_index_cvi_pct']} %")
    print(f"  L/S Ratio:   {normal_case['choroidal_metrics']['luminal_to_stromal_ratio']}")
    print(f"  Diagnosis:   {normal_case['clinical_diagnosis']['choroidal_state']}")

    print("\n=== Case 2: Pachychoroid Spectrum / Central Serous Chorioretinopathy ===")
    pachy_case = client.evaluate_cvi(
        subfoveal_choroidal_thickness_um=420.0,
        total_choroidal_area_mm2=1.95,
        luminal_area_mm2=1.42,
        patient_age_years=38,
        axial_length_mm=23.2,
        eye_examined="OS"
    )
    print("Choroidal Morphology:")
    print(f"  SFCT:        {pachy_case['choroidal_metrics']['subfoveal_thickness_sfct_um']} um (Markedly thickened!)")
    print(f"  CVI:         {pachy_case['choroidal_metrics']['choroidal_vascularity_index_cvi_pct']} %")
    print(f"  L/S Ratio:   {pachy_case['choroidal_metrics']['luminal_to_stromal_ratio']}")
    print(f"  Diagnosis:   {pachy_case['clinical_diagnosis']['choroidal_state']}")
    print(f"  Risk:        {pachy_case['clinical_diagnosis']['clinical_pathophysiology']}")

if __name__ == "__main__":
    main()
