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
- AIF-SFDA: Autonomous Information Filter-driven Source-Free Domain Adaptation for Medical Image Segmentation (AAAI 2025) [[arxiv](https://arxiv.org/abs/2501.03074)] [[code](https://github.com/JingHuaMan/AIF-SFDA)]
- Distinguish Then Exploit: Source-free Open Set Domain Adaptation via Weight Barcode Estimation and Sparse Label Assignment (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.html)] [[pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.pdf)]
- Effective dual-region augmentation for reduced reliance on large amounts of labeled data (2025) [[paper](https://doi.org/10.1117/12.3058627)] [[code](https://github.com/PrasannaPulakurthi/Foreground-Background-Augmentation)]
- ElimPCL: Eliminating Noise Accumulation with Progressive Curriculum Labeling for Source-Free Domain Adaptation (arXiv 2025) [[arxiv](https://arxiv.org/abs/2503.23712)]
- Label Calibration in Source Free Domain Adaptation (WACV 2025) [[paper](https://openaccess.thecvf.com/content/WACV2025/html/Rai_Label_Calibration_in_Source_Free_Domain_Adaptation_WACV_2025_paper.html)] [[arxiv](https://arxiv.org/abs/2501.07072)]
- Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Multi-Granularity_Class_Prototype_Topology_Distillation_for_Class-Incremental_Source-Free_Unsupervised_Domain_CVPR_2025_paper.html)]
- Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimal_Transport-Guided_Source-Free_Adaptation_for_Face_Anti-Spoofing_CVPR_2025_paper.html)] [[arxiv](https://arxiv.org/abs/2503.22984)]
- PointSFDA: Source-free Domain Adaptation for Point Cloud Completion (arXiv 2025) [[arxiv](https://arxiv.org/abs/2503.15144)] [[code](https://github.com/Starak-x/PointSFDA)]
- ProSFDA: Source-free Domain Adaptation Using Prompt Learning for Medical Image Segmentation (Pattern Recognition 2025) [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325009513)] [[code](https://github.com/ShishuaiHu/ProSFDA)]
- Proxy Denoising for Source-Free Domain Adaptation (ICLR 2025) [[paper](https://openreview.net/forum?id=FIj9IEPCKr)] [[arxiv](https://arxiv.org/abs/2406.01658)]
- Revisiting Source-Free Domain Adaptation: a New Perspective via Uncertainty Control (ICLR 2025) [[paper](https://openreview.net/pdf?id=nx9Z5Kva96)] [[code](https://github.com/xugezheng/UCon_SFDA)]
- Revisiting Source-Free Domain Adaptation: Insights into Representativeness, Generalization, and Variety (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Revisiting_Source-Free_Domain_Adaptation_Insights_into_Representativeness_Generalization_and_Variety_CVPR_2025_paper.html)]
- Shuffle PatchMix Augmentation with Confidence-Margin Weighted Pseudo-Labels for Enhanced Source-Free Domain Adaptation (ICIP 2025) [[arxiv](https://arxiv.org/abs/2505.24216)] [[code](https://github.com/PrasannaPulakurthi/SPM)]
- Source-free Video Domain Adaptation by Learning from Noisy Labels (Pattern Recognition 2025) [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320324010793)] [[code](https://github.com/avijit9/CleanAdapt)]
- Unraveling the Mysteries of Label Noise in Source-Free Domain Adaptation: Theory and Practice (TPAMI 2025) [[paper](https://www.computer.org/csdl/journal/tp/2025/05/10858421/23VPxGAlL4Q)] [[code](https://github.com/xugezheng/labelNoiseInSFDA)]
- VP-SFDA: Visual Prompt Source-Free Domain Adaptation for Cross-Modal Medical Image Segmentation (Health Data Science 2025) [[paper](https://spj.science.org/doi/10.34133/hds.0143)]

### 2024
- A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) [[paper](https://ieeexplore.ieee.org/document/10452835)] [[arxiv](https://arxiv.org/abs/2302.11803)]
- Aligning Non-Causal Factors for Transformer-Based Source-Free Domain Adaptation (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/html/Sanyal_Aligning_Non-Causal_Factors_for_Transformer-Based_Source-Free_Domain_Adaptation_WACV_2024_paper.html)]
- De-Confusing Pseudo-Labels in Source-Free Domain Adaptation (ECCV 2024) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10138.pdf)] [[arxiv](https://arxiv.org/abs/2401.01650)] [[code](https://github.com/ssi-research/DCPL_SFDA)]
- EventDance: Unsupervised Source-free Cross-modal Adaptation for Event-based Object Recognition (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zheng_EventDance_Unsupervised_Source-free_Cross-modal_Adaptation_for_Event-based_Object_Recognition_CVPR_2024_paper.pdf)] [[code](https://github.com/zhengxujosh/EventDance)]
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) [[paper](https://ieeexplore.ieee.org/document/10561561)]
- Hierarchical Unsupervised Relation Distillation for Source-Free Domain Adaptation (ECCV 2024) [[paper](https://eccv.ecva.net/virtual/2024/poster/1198)]
- Neighborhood-Aware Mutual Information Maximization for SFDA (TMM 2024) [[paper](https://ieeexplore.ieee.org/document/10510655)]
- ReCLIP: Refine Contrastive Language Image Pre-Training with SFDA (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/papers/Hu_ReCLIP_Refine_Contrastive_Language_Image_Pre-Training_With_Source_Free_Domain_WACV_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2308.03793)] [[code](https://github.com/michiganleon/ReCLIP_WACV)]
- Robust Nearest Neighbors for Source-Free Domain Adaptation under Class Distribution Shift (ECCV 2024) [[paper](https://eccv.ecva.net/virtual/2024/poster/833)] [[code](https://github.com/CyberAgentAILab/Robust_Nearest_Neighbors_SFDA-CDS)]
- Robust Source-Free Domain Adaptation for Fundus Image Segmentation (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/papers/Li_Robust_Source-Free_Domain_Adaptation_for_Fundus_Image_Segmentation_WACV_2024_paper.pdf)] [[code](https://github.com/LinGrayy/PLPB)]
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) [[paper](https://arxiv.org/abs/2402.08249)]
- SF(DA)²: Source-free Domain Adaptation Through the Lens of Data Augmentation (ICLR 2024) [[paper](https://openreview.net/pdf?id=kUCgHbmO11)] [[arxiv](https://arxiv.org/abs/2312.08566)] [[code](https://github.com/shinyflight/SFDA2)]
- SFDA for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) [[paper](https://arxiv.org/abs/2305.14269)]
- SFDA with Diffusion-Guided Source Data Generation (arXiv 2024) [[paper](https://arxiv.org/abs/2402.04929)]
- SFDA with Frozen Multimodal Foundation Model (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Tang_Source-Free_Domain_Adaptation_with_Frozen_Multimodal_Foundation_Model_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2311.16510)]
- Simplifying Source-Free Domain Adaptation for Object Detection (ECCV 2024) [[paper](https://link.springer.com/chapter/10.1007/978-3-031-72949-2_12)] [[arxiv](https://arxiv.org/abs/2407.07586)] [[code](https://github.com/EPFL-IMOS/simple-SFOD)]
- Stable Neighbor Denoising for Source-free Domain Adaptive Segmentation (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_Stable_Neighbor_Denoising_for_Source-free_Domain_Adaptive_Segmentation_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2406.06813)] [[code](https://github.com/DZhaoXd/SND)]
- Towards Stable and Robust Source-free Unsupervised 3D Semantic Segmentation (ECCV 2024) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02968.pdf)]
- Uncertainty-Aware Source-Free Adaptive Image Super-Resolution with Wavelet Augmentation Transformer (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Ai_Uncertainty-Aware_Source-Free_Adaptive_Image_Super-Resolution_with_Wavelet_Augmentation_Transformer_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2303.17783)] [[code](https://github.com/shallowdream204/SODA-SR)]
- Understanding and Improving Source-free Domain Adaptation from a Theoretical Perspective (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/html/Mitsuzumi_Understanding_and_Improving_Source-free_Domain_Adaptation_from_a_Theoretical_Perspective_CVPR_2024_paper.html)] [[code](https://github.com/nttcslab/improved_sfda)]
- Unveiling the Unknown: Unleashing the Power of Unknown to Known in Open-Set Source-Free Domain Adaptation (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Wan_Unveiling_the_Unknown_Unleashing_the_Power_of_Unknown_to_Known_CVPR_2024_paper.pdf)] [[code](https://github.com/xdwfl/UPUK)]
- Visually Source-Free Domain Adaptation via Adversarial Style Matching (TIP 2024) [[paper](https://ieeexplore.ieee.org/document/10410236)]

## Datasets & Benchmarks
- [Office-31](https://drive.google.com/file/d/0B4IapRTv9pJ1WGZVd1VDMmhwdlE/view?resourcekey=0-gNMHVtZfRAyO_t2_WrOunA)
- [Office-Home](https://drive.google.com/file/d/0B81rNlvomiwed0V1YUxQdC1uOTg/view)
- [VISDA-C](https://github.com/VisionLearningGroup/taskcv-2017-public/tree/master/classification)
- [DomainNet (cleaned)](http://ai.bu.edu/M3SDA/)
- [PACS](https://domaingeneralization.github.io/)
- [ImageNet-A](https://github.com/hendrycks/natural-adv-examples)
- [ImageNet-R](https://github.com/hendrycks/imagenet-r)
- [ImageNet-V2](https://huggingface.co/datasets/vaishaal/ImageNetV2/tree/main)
- [ImageNet-Sketch](https://github.com/HaohanWang/ImageNet-Sketch)

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
