---
name: genpark-personal-agent-ocular-choroidal-vascularity-index-cvi-oct-skill
version: 1.0.0
description: Calculates EDI/SS-OCT Choroidal Vascularity Index (CVI = LA/TCA * 100), Subfoveal Choroidal Thickness (SFCT), and pachychoroid vs choroidal atrophy classification.
license: Apache-2.0
compatibility:
  python: ">=3.9"
  openclaw: ">=1.0.0"
  mcp: ">=1.0.0"
---

# Ocular Choroidal Vascularity Index (CVI) & Subfoveal Choroidal Thickness Skill

A zero-dependency personal agent skill for evaluating choroidal microvascular architecture, luminal-to-stromal proportion, and differentiating pachychoroid spectrum disease from atrophic choroidopathy via binarized EDI/SS-OCT.

## Features
- **Choroidal Vascularity Index ($CVI\%$)**: Computes ratio of vascular luminal area to total choroidal area ($LA / TCA \times 100\%$).
- **Subfoveal Choroidal Thickness ($SFCT$)**: Assesses perpendicular foveal choroidal thickness with age-adjusted normative comparison.
- **Luminal/Stromal Ratio ($L/S$)**: Quantifies vascular density against connective tissue interstitial stroma.
- **Pachychoroid vs Atrophy Stratification**: Detects pachychoroid spectrum ($CVI > 70\%, SFCT > 360\ \mu m$) and myopic/AMD choroidal atrophy ($CVI < 60\%, SFCT < 150\ \mu m$).

## MCP Server Integration
Exposes `evaluate_cvi` for autonomous retinal microvascular wellness, digital eye strain, and macular health monitoring.
