# Awesome Source‑Free Domain Adaptation (SFDA) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated resources for Source‑Free Domain Adaptation (SFDA): methods that adapt using only a trained source model (no source data). Includes papers, code, datasets, benchmarks, and tutorials.
<!--lint disable awesome-github repo-url -->

## Contents
- [Papers](#papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Libraries & Tooling](#libraries--tooling)
- [Tutorials & Talks](#tutorials--talks)

## Papers
## 2025
- AIF-SFDA: Autonomous Information Filter-driven Source-Free Domain Adaptation for Medical Image Segmentation (AAAI 2025) [[arXiv](https://arxiv.org/abs/2408.05038)] [[Code](https://github.com/hust-ljx/AIF-SFDA)]
- Distinguish Then Exploit: Source-free Open Set Domain Adaptation via Weight Barcode Estimation and Sparse Label Assignment (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.html)] [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.pdf)]
- Effective dual-region augmentation for reduced reliance on large amounts of labeled data (2025) [[Paper](https://doi.org/10.1117/12.3058627)] [[Code](https://github.com/PrasannaPulakurthi/Foreground-Background-Augmentation)]
- ElimPCL: Eliminating Noise Accumulation with Progressive Curriculum Labeling for Source-Free Domain Adaptation (arXiv 2025) [[arXiv](https://arxiv.org/abs/2503.23712)]
- Label Calibration in Source Free Domain Adaptation (WACV 2025) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Rai_Label_Calibration_in_Source_Free_Domain_Adaptation_WACV_2025_paper.html)] [[arXiv](https://arxiv.org/abs/2501.07072)]
- Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Multi-Granularity_Class_Prototype_Topology_Distillation_for_Class-Incremental_Source-Free_Unsupervised_Domain_CVPR_2025_paper.html)]
- Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimal_Transport-Guided_Source-Free_Adaptation_for_Face_Anti-Spoofing_CVPR_2025_paper.html)] [[arXiv](https://arxiv.org/abs/2503.22984)]
- PointSFDA: Source-free Domain Adaptation for Point Cloud Completion (arXiv 2025) [[arXiv](https://arxiv.org/abs/2503.15144)] [[Code](https://github.com/Starak-x/PointSFDA)]
- ProSFDA: Source-free Domain Adaptation Using Prompt Learning for Medical Image Segmentation (Pattern Recognition 2025) [[Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325001385)] [[arXiv](https://arxiv.org/abs/2404.16696)] [[Code](https://github.com/zs-26/ProSFDA)]
- Proxy Denoising for Source-Free Domain Adaptation (ICLR 2025) [[Paper](https://openreview.net/forum?id=FIj9IEPCKr)] [[arXiv](https://arxiv.org/abs/2406.01658)]
- Revisiting Source-Free Domain Adaptation: a New Perspective via Uncertainty Control (ICLR 2025) [[Paper](https://openreview.net/pdf?id=nx9Z5Kva96)] [[Code](https://github.com/xugezheng/UCon_SFDA)]
- Revisiting Source-Free Domain Adaptation: Insights into Representativeness, Generalization, and Variety (CVPR 2025) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Revisiting_Source-Free_Domain_Adaptation_Insights_into_Representativeness_Generalization_and_Variety_CVPR_2025_paper.html)]
- Shuffle PatchMix Augmentation with Confidence-Margin Weighted Pseudo-Labels for Enhanced Source-Free Domain Adaptation (ICIP 2025) [[arXiv](https://arxiv.org/abs/2505.24216)] [[Code](https://github.com/PrasannaPulakurthi/SPM)]
- Source-free Video Domain Adaptation by Learning from Noisy Labels (Pattern Recognition 2025) [[Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320324010793)] [[Project](https://avijit9.github.io/CleanAdapt/)] [[Code](https://github.com/avijit9/CleanAdapt)]
- Unraveling the Mysteries of Label Noise in Source-Free Domain Adaptation: Theory and Practice (TPAMI 2025) [[Paper](https://www.computer.org/csdl/journal/tp/2025/05/10858421/23VPxGAlL4Q)] [[Code](https://github.com/xugezheng/labelNoiseInSFDA)]
- VP-SFDA: Visual Prompt Source-Free Domain Adaptation for Cross-Modal Medical Image Segmentation (Health Data Science 2025) [[Paper](https://academic.oup.com/hdsr/article/7/1/2025/7688831)]

## 2024
- A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) [[Paper](https://ieeexplore.ieee.org/document/10533539)] [[arXiv](https://arxiv.org/abs/2302.11803)]
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) [[Paper](https://ieeexplore.ieee.org/document/10405692)] [[arXiv](https://arxiv.org/abs/2307.08740)] [[Code](https://github.com/Jerry-Luo-98/GALA)]
- Neighborhood-Aware Mutual Information Maximization for SFDA (TMM 2024) [[Paper](https://ieeexplore.ieee.org/document/10603809)] [[arXiv](https://arxiv.org/abs/2403.18239)]
- ReCLIP: Refine Contrastive Language Image Pre-Training with SFDA (WACV 2024) [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Yao_ReCLIP_Refine_Contrastive_Language_Image_Pre-Training_with_Source-Free_Domain_Adaptation_WACV_2024_paper.html)] [[arXiv](https://arxiv.org/abs/2310.10893)] [[Code](https://github.com/parasol-team/reclip)]
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) [[Paper](https://arxiv.org/abs/2402.08249)]
- SF(DA)²: Source-free Domain Adaptation Through the Lens of Data Augmentation (ICLR 2024) [[Paper](https://openreview.net/forum?id=4WJ1X0XyBI)] [[arXiv](https://arxiv.org/abs/2312.08566)] [[Code](https://github.com/shinyflight/SFDA2)]
- SFDA for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) [[Paper](https://arxiv.org/abs/2406.19533)]
- SFDA with Diffusion-Guided Source Data Generation (arXiv 2024) [[Paper](https://arxiv.org/abs/2401.12047)]
- SFDA with Frozen Multimodal Foundation Model (CVPR 2024) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Source-Free_Domain_Adaptation_with_Frozen_Multimodal_Foundation_Model_CVPR_2024_paper.html)] [[arXiv](https://arxiv.org/abs/2403.11066)] [[Code](https://github.com/tntek/source-free-domain-adaptation)]
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
