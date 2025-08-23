# Awesome Source‑Free Domain Adaptation (SFDA) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated resources for Source‑Free Domain Adaptation (SFDA): methods that adapt using only a trained source model (no source data). Includes papers, code, datasets, benchmarks, and tutorials.
<!--lint disable awesome-github repo-url -->

## Contents
- [Papers](#papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Libraries & Tooling](#libraries--tooling)
- [Tutorials & Talks](#tutorials--talks)

## Papers
### 2025 
- Revisiting Source-Free Domain Adaptation: Insights into Representativeness, Generalization, and Variety (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Revisiting_Source-Free_Domain_Adaptation_Insights_into_Representativeness_Generalization_and_Variety_CVPR_2025_paper.html)]
- Distinguish Then Exploit: Source-free Open Set Domain Adaptation via Weight Barcode Estimation and Sparse Label Assignment (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Distinguish_Then_Exploit_Source-Free_Open_Set_Domain_Adaptation_via_Weight_Barcode_Estimation_CVPR_2025_paper.html)]
- Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing (CVPR 2025) [[arXiv](https://arxiv.org/abs/2503.22984)] [[Paper](https://cvpr.thecvf.com/virtual/2025/poster/33252)]
- Proxy Denoising for Source-Free Domain Adaptation (ICLR 2025 Oral) [[Paper](https://openreview.net/forum?id=FIj9IEPCKr)] [[Code](https://github.com/tntek/source-free-domain-adaptation)]
- Revisiting Source-Free Domain Adaptation: a New Perspective via Uncertainty Control (ICLR 2025 Poster) [[Paper](https://openreview.net/forum?id=nx9Z5Kva96)] [[Code](https://github.com/xugezheng/UCon_SFDA)]
- What Has Been Overlooked in Contrastive Source-Free Domain Adaptation: Leveraging Source-Informed Latent Augmentation within Neighborhood Context (ICLR 2025 Journal Track/TMLR) [[Paper](https://openreview.net/forum?id=iulMde3dP1)] [[Code](https://github.com/JingWang18/SiLAN)]
- Source-Free Domain Adaptation via Multi-view Contrastive Learning (arXiv 2025) [[arXiv](https://arxiv.org/abs/2507.03321)]
- ElimPCL: Eliminating Noise Accumulation with Progressive Curriculum Labeling for SFDA (arXiv 2025) [[arXiv](https://arxiv.org/abs/2503.23712)]
- Unraveling the Mysteries of Label Noise in SFDA: Theory and Practice (TPAMI 2025) [[Paper](https://www.computer.org/csdl/journal/tp/2025/05/10858421/23VPxGAlL4Q)] [[Code](https://github.com/xugezheng/labelNoiseInSFDA)]
- Temporal Source Recovery for Time-Series Source-Free UDA (ICLR 2025 submission) [[Paper](https://openreview.net/forum?id=GhM63V7z6v)]
- VP-SFDA (Health Data Science 2025) [[Paper](https://link.springer.com/article/10.1007/s42399-025-00184-9)]
- ProSFDA (Pattern Recognition 2025) [[Paper](https://www.sciencedirect.com/science/article/pii/S0031320320301556)] [[arXiv](https://arxiv.org/abs/2207.09823)] [[Code](https://github.com/ProSFDA)]

### 2024
- A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) [[Paper](https://ieeexplore.ieee.org/document/10533539)] [[arXiv](https://arxiv.org/abs/2302.11803)]
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) [[Paper](https://ieeexplore.ieee.org/document/10405692)] [[arXiv](https://arxiv.org/abs/2307.08740)] [[Code](https://github.com/Jerry-Luo-98/GALA)]
- Neighborhood-Aware Mutual Information Maximization for SFDA (TMM 2024) [[Paper](https://ieeexplore.ieee.org/document/10603809)] [[arXiv](https://arxiv.org/abs/2403.18239)]
- ReCLIP: Refine Contrastive Language Image Pre-Training with SFDA (WACV 2024) [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Yao_ReCLIP_Refine_Contrastive_Language_Image_Pre-Training_with_Source-Free_Domain_Adaptation_WACV_2024_paper.html)] [[arXiv](https://arxiv.org/abs/2310.10893)] [[Code](https://github.com/parasol-team/reclip)]
- SF(DA)²: Source-free Domain Adaptation Through the Lens of Data Augmentation (ICLR 2024) [[Paper](https://openreview.net/forum?id=4WJ1X0XyBI)] [[arXiv](https://arxiv.org/abs/2312.08566)] [[Code](https://github.com/shinyflight/SFDA2)]
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) [[Paper](https://arxiv.org/abs/2402.08249)]
- SFDA for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) [[Paper](https://arxiv.org/abs/2406.19533)]
- SFDA with Diffusion-Guided Source Data Generation (arXiv 2024) [[Paper](https://arxiv.org/abs/2401.12047)]
- SFDA with Frozen Multimodal Foundation Model (CVPR 2024) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Source-Free_Domain_Adaptation_with_Frozen_Multimodal_Foundation_Model_CVPR_2024_paper.html)] [[arXiv](https://arxiv.org/abs/2403.11066)] [[Code (repo incl. DIFO)](https://github.com/tntek/source-free-domain-adaptation)]
- Understanding and Improving SFDA from a Theoretical Perspective (CVPR 2024) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Kawasaki_Understanding_and_Improving_Source-free_Domain_Adaptation_from_a_Theoretical_Perspective_CVPR_2024_paper.html)] [[arXiv](https://arxiv.org/abs/2403.15957)] [[Code](https://github.com/nttcslab/improved_sfda)]
- Visually Source-Free Domain Adaptation via Adversarial Style Matching (TIP 2024) [[Paper](https://ieeexplore.ieee.org/document/10424442)]

## Datasets & Benchmarks
- DomainNet — multi‑domain classification benchmark.
- Office‑31 / Office‑Home — classic DA suites, widely reused in SFDA.
- VisDA‑2017 — synthetic→real; used by SFDA methods.

## Libraries & Tooling
- Add libraries and tooling here.

## Tutorials & Talks
- Add tutorials and talks here.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md). Use this entry format:

```
- Title (Venue/Year) [[paper](https://example.com/paper)] [[code](https://example.com/code)] [[project](https://example.com/site)]
```

Sorting policy:
- Sort entries alphabetically by title within each section.
