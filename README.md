# Awesome Source‑Free Domain Adaptation (SFDA) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Verify citations](https://github.com/PrasannaPulakurthi/really-awesome-sfda/actions/workflows/verify-citations.yml/badge.svg)](https://github.com/PrasannaPulakurthi/really-awesome-sfda/actions/workflows/verify-citations.yml)
[![Link check](https://github.com/PrasannaPulakurthi/really-awesome-sfda/actions/workflows/link-check.yml/badge.svg)](https://github.com/PrasannaPulakurthi/really-awesome-sfda/actions/workflows/link-check.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Source-free domain adaptation** adapts a model to a new domain using only the
trained source model — no source data, because it is often private, proprietary
or simply too large to ship. This list covers SFDA and its neighbours:
test-time adaptation, open-set and continual variants, federated settings, and
the applications they are actually deployed in.

**Every citation here is machine-verified.** Each pull request resolves the
entry's identifiers against publisher records — arXiv, Crossref, and the
proceedings pages of CVF, PMLR, NeurIPS, AAAI and IJCAI — and checks that the
venue, the year and the linked repository all match what the record says. An
entry nothing can confirm is reported as unverified rather than quietly
accepted. Wrong venues and dead links are the usual failure of a paper list, and
this one is built to catch them.

Papers are listed newest first, tagged with venue and year, and linked to code
wherever it exists.

<!--lint disable awesome-github repo-url -->

## Contents
- [Surveys & Theory](#surveys--theory)
- [Applications](#applications)
  - [Image Classification](#image-classification)
  - [Object Detection](#object-detection)
  - [Semantic Segmentation (2D)](#semantic-segmentation-2d)
  - [Remote Sensing](#remote-sensing)
  - [Landmine Detection](#landmine-detection)
  - [3D / Point Cloud](#3d--point-cloud)
  - [Medical Imaging](#medical-imaging)
  - [Video / Action Recognition](#video--action-recognition)
  - [Person Re-Identification](#person-re-identification)
  - [Face Anti-Spoofing](#face-anti-spoofing)
  - [Facial Expression / Emotion Recognition](#facial-expression--emotion-recognition)
  - [Human Pose Estimation](#human-pose-estimation)
  - [Image Super-Resolution](#image-super-resolution)
  - [Time Series & Signals](#time-series--signals)
- [Settings & Extensions](#settings--extensions)
  - [Test-Time Adaptation (TTA)](#test-time-adaptation-tta)
  - [Open-Set / Class Distribution Shift](#open-set--class-distribution-shift)
  - [Continual / Class-Incremental SFDA](#continual--class-incremental-sfda)
  - [Multi-Source SFDA](#multi-source-sfda)
  - [Federated SFDA](#federated-sfda)
  - [Active SFDA](#active-sfda)
  - [Cross-Domain Few-Shot](#cross-domain-few-shot)
  - [Cross-Modal SFDA](#cross-modal-sfda)
  - [Foundation Models / VLM-based](#foundation-models--vlm-based)
  - [Noisy Labels in SFDA](#noisy-labels-in-sfda)
  - [Security / Privacy](#security--privacy)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contribution](#contribution)

Within each section, entries are sorted by year (descending) and then alphabetically by title.

## Surveys & Theory
- Vicinal Gaussian Transform: Rethinking Source-Free Domain Adaptation Through Source-Informed Label Consistency [`paper`](https://doi.org/10.1109/TPAMI.2025.3621631) `TPAMI'26`
- CLIP-Powered Domain Generalization and Domain Adaptation: A Comprehensive Survey [`paper`](https://doi.org/10.1109/tpami.2026.3651700) [`arxiv`](https://arxiv.org/abs/2504.14280) `TPAMI'26`
- Unraveling the Mysteries of Label Noise in Source-Free Domain Adaptation: Theory and Practice [`paper`](https://doi.org/10.1109/tpami.2025.3536845) [`code`](https://github.com/xugezheng/labelNoiseInSFDA) `TPAMI'25` [![Stars](https://img.shields.io/github/stars/xugezheng/labelNoiseInSFDA?style=social)](https://github.com/xugezheng/labelNoiseInSFDA)
- A Comprehensive Survey on Source-Free Domain Adaptation [`paper`](https://ieeexplore.ieee.org/document/10452835) [`arxiv`](https://arxiv.org/abs/2302.11803) `TPAMI'24`
- Understanding and Improving Source-free Domain Adaptation from a Theoretical Perspective [`paper`](https://openaccess.thecvf.com/content/CVPR2024/html/Mitsuzumi_Understanding_and_Improving_Source-free_Domain_Adaptation_from_a_Theoretical_Perspective_CVPR_2024_paper.html) [`code`](https://github.com/nttcslab/improved_sfda) `CVPR'24` [![Stars](https://img.shields.io/github/stars/nttcslab/improved_sfda?style=social)](https://github.com/nttcslab/improved_sfda)
- Unveiling the Superior Paradigm: A Comparative Study of Source-Free Domain Adaptation and Unsupervised Domain Adaptation [`arxiv`](https://arxiv.org/abs/2411.15844) `arXiv'24`

## Applications

### Image Classification
- CCST: Cross-Modal and Consistency-Aware Self-Training for Source-Free Unsupervised Domain Adaptation in Speech Recognition [`paper`](https://ieeexplore.ieee.org/abstract/document/11461841) `ICASSP'26`
- Attention Residual Fusion Network with Contrast for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2510.22142) `TCSVT'26`
- COSMO: Consensus-Driven Shift Modulation for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2608.04604) `arXiv'26`
- ME-SFDA: Marginal Exploration with Pyramidal Atkinson-Shiffrin Memory for Source-Free Domain Adaptation [`paper`](https://doi.org/10.1609/aaai.v40i28.39539) `AAAI'26`
- Measure The Feature Universe: Topology-based Pseudo Labeling and Gravity Consistency for Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Measure_The_Feature_Universe_Topology-based_Pseudo_Labeling_and_Gravity_Consistency_CVPR_2026_paper.html) `CVPR'26`
- ProCal: Probability Calibration for Neighborhood-Guided Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2603.18764) `arXiv'26`
- Robust Source-Free Domain Adaptation From Non-Robust Source Models [`paper`](https://doi.org/10.1109/TIP.2026.3661392) `TIP'26`
- SfMamba: Efficient Source-Free Domain Adaptation via Selective Scan Modeling [`arxiv`](https://arxiv.org/abs/2601.08608) `Expert Systems with Applications'26`
- Source-Free Domain Adaptation by Optimizing Batch-Wise Cosine Similarity [`arxiv`](https://arxiv.org/abs/2601.17408) `arXiv'26`
- A Source-Free Approach for Domain Adaptation via Multiview Image Transformation and Latent Space Consistency [`arxiv`](https://arxiv.org/abs/2601.20284) `arXiv'26`
- A Tale of Two Experts: Cooperative Learning for Source-Free Unsupervised Domain Adaptation [`arxiv`](https://arxiv.org/abs/2509.22229) `arXiv'25`
- Consistent Assistant Domains Transformer for Source-Free Domain Adaptation [`paper`](https://doi.org/10.1109/TIP.2025.3611799) [`arxiv`](https://arxiv.org/abs/2510.01559) `TIP'25`
- Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation [`paper`](https://papers.nips.cc/paper_files/paper/2025/hash/9cf6139382f98623d08cc595622f3fb1-Abstract-Conference.html) [`arxiv`](https://arxiv.org/abs/2510.25279) `NeurIPS'25`
- Domain-Division Based Progressive Learning for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2607.29202) `TMM'25`
- DUET: Dual-Perspective Pseudo Labeling and Uncertainty-aware Exploration & Exploitation Training for Source-Free Domain Adaptation [`paper`](https://papers.nips.cc/paper_files/paper/2025/hash/6c8dfbbd1ba3e22339e58a336cbed52b-Abstract-Conference.html) `NeurIPS'25`
- Effective dual-region augmentation for reduced reliance on large amounts of labeled data (2025) [`paper`](https://doi.org/10.1117/12.3058627) [`arxiv`](https://arxiv.org/abs/2504.13077) [`code`](https://github.com/PrasannaPulakurthi/Foreground-Background-Augmentation) [![Stars](https://img.shields.io/github/stars/PrasannaPulakurthi/Foreground-Background-Augmentation?style=social)](https://github.com/PrasannaPulakurthi/Foreground-Background-Augmentation)
- Energy-Based Pseudo-Label Refining for Source-free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2504.16692) [`code`](https://github.com/Sthen111/EBPR) `Pattern Recognition Letters'25` [![Stars](https://img.shields.io/github/stars/Sthen111/EBPR?style=social)](https://github.com/Sthen111/EBPR)
- Grad-CL: Source Free Domain Adaptation with Gradient Guided Feature Disalignment [`arxiv`](https://arxiv.org/abs/2509.10134) `BMVC'25`
- Label Calibration in Source Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/WACV2025/html/Rai_Label_Calibration_in_Source_Free_Domain_Adaptation_WACV_2025_paper.html) [`arxiv`](https://arxiv.org/abs/2501.07072) `WACV'25`
- Proxy Denoising for Source-Free Domain Adaptation [`paper`](https://openreview.net/forum?id=FIj9IEPCKr) [`arxiv`](https://arxiv.org/abs/2406.01658) `ICLR'25`
- Revisiting Source-Free Domain Adaptation: a New Perspective via Uncertainty Control [`paper`](https://openreview.net/pdf?id=nx9Z5Kva96) [`code`](https://github.com/xugezheng/UCon_SFDA) `ICLR'25` [![Stars](https://img.shields.io/github/stars/xugezheng/UCon_SFDA?style=social)](https://github.com/xugezheng/UCon_SFDA)
- Revisiting Source-Free Domain Adaptation: Insights into Representativeness, Generalization, and Variety [`paper`](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Revisiting_Source-Free_Domain_Adaptation_Insights_into_Representativeness_Generalization_and_Variety_CVPR_2025_paper.html) `CVPR'25`
- Shuffle PatchMix Augmentation with Confidence-Margin Weighted Pseudo-Labels for Enhanced Source-Free Domain Adaptation [`paper`](https://ieeexplore.ieee.org/document/11084606) [`arxiv`](https://arxiv.org/abs/2505.24216) [`code`](https://github.com/PrasannaPulakurthi/SPM) `ICIP'25` [![Stars](https://img.shields.io/github/stars/PrasannaPulakurthi/SPM?style=social)](https://github.com/PrasannaPulakurthi/SPM)
- Source-Free Domain Adaptation via Multi-view Contrastive Learning [`paper`](https://doi.org/10.1007/s11227-026-08460-2) [`arxiv`](https://arxiv.org/abs/2507.03321) `J. Supercomputing'26`
- What Has Been Overlooked in Contrastive Source-Free Domain Adaptation: Leveraging Source-Informed Latent Augmentation within Neighborhood Context [`arxiv`](https://arxiv.org/abs/2412.14301) `ICLR'25`
- Aligning Non-Causal Factors for Transformer-Based Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/WACV2024/html/Sanyal_Aligning_Non-Causal_Factors_for_Transformer-Based_Source-Free_Domain_Adaptation_WACV_2024_paper.html) `WACV'24`
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation [`paper`](https://ieeexplore.ieee.org/document/10561561) `TPAMI'24`
- Hierarchical Unsupervised Relation Distillation for Source-Free Domain Adaptation [`paper`](https://eccv.ecva.net/virtual/2024/poster/1198) `ECCV'24`
- Neighborhood-Aware Mutual Information Maximization for Source-Free Domain Adaptation [`paper`](https://doi.org/10.1109/tmm.2024.3394971) `TMM'24`
- SF(DA)²: Source-free Domain Adaptation Through the Lens of Data Augmentation [`paper`](https://openreview.net/pdf?id=kUCgHbmO11) [`arxiv`](https://arxiv.org/abs/2312.08566) [`code`](https://github.com/shinyflight/SFDA2) `ICLR'24` [![Stars](https://img.shields.io/github/stars/shinyflight/SFDA2?style=social)](https://github.com/shinyflight/SFDA2)
- SFDA with Diffusion-Guided Source Data Generation [`paper`](https://arxiv.org/abs/2402.04929) `arXiv'24`
- Visually Source-Free Domain Adaptation via Adversarial Style Matching [`paper`](https://ieeexplore.ieee.org/document/10410236) `TIP'24`
- Class Relationship Embedded Learning for Source-Free Unsupervised Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_Class_Relationship_Embedded_Learning_for_Source-Free_Unsupervised_Domain_Adaptation_CVPR_2023_paper.html) [`code`](https://github.com/zhyx12/CRCo) `CVPR'23` [![Stars](https://img.shields.io/github/stars/zhyx12/CRCo?style=social)](https://github.com/zhyx12/CRCo)
- Domain-Specificity Inducing Transformers for Source-Free Domain Adaptation (DSiT) [`arxiv`](https://arxiv.org/abs/2308.14023) `ICCV'23`
- Guiding Pseudo-Labels with Uncertainty Estimation for Source-Free Unsupervised Domain Adaptation (PLUE) [`paper`](https://openaccess.thecvf.com/content/CVPR2023/html/Litrico_Guiding_Pseudo-Labels_With_Uncertainty_Estimation_for_Source-Free_Unsupervised_Domain_Adaptation_CVPR_2023_paper.html) `CVPR'23`
- Rethinking the Role of Pre-Trained Networks in Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Rethinking_the_Role_of_Pre-Trained_Networks_in_Source-Free_Domain_Adaptation_ICCV_2023_paper.html) `ICCV'23`
- Source-Free Domain Adaptation via Target Prediction Distribution Searching (TPDS) [`paper`](https://link.springer.com/article/10.1007/s11263-023-01892-w) `IJCV'23`
- Adaptive Contrastive Learning with Label Consistency for Source Data Free Unsupervised Domain Adaptation [`paper`](https://pmc.ncbi.nlm.nih.gov/articles/PMC9185254/) `Sensors'22`
- Attracting and Dispersing: A Simple Approach for Source-free Domain Adaptation (AaD) [`arxiv`](https://arxiv.org/abs/2205.04183) [`code`](https://github.com/Albert0147/AaD_SFDA) `NeurIPS'22` [![Stars](https://img.shields.io/github/stars/Albert0147/AaD_SFDA?style=social)](https://github.com/Albert0147/AaD_SFDA)
- Balancing Discriminability and Transferability for Source-Free Domain Adaptation [`paper`](https://proceedings.mlr.press/v162/kundu22a.html) `ICML'22`
- Confidence Score for Source-Free Unsupervised Domain Adaptation (CoWA) [`paper`](https://proceedings.mlr.press/v162/lee22c.html) `ICML'22`
- Divide and Contrast: Source-free Domain Adaptation via Adaptive Contrastive Learning (DaC) [`arxiv`](https://arxiv.org/abs/2211.06612) [`code`](https://github.com/ZyeZhang/DaC) `NeurIPS'22` [![Stars](https://img.shields.io/github/stars/ZyeZhang/DaC?style=social)](https://github.com/ZyeZhang/DaC)
- Exploring Domain-Invariant Parameters for Source Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Exploring_Domain-Invariant_Parameters_for_Source_Free_Domain_Adaptation_CVPR_2022_paper.html) `CVPR'22`
- Model Adaptation: Historical Contrastive Learning for Unsupervised Domain Adaptation without Source Data (HCL) [`arxiv`](https://arxiv.org/abs/2110.03374) `NeurIPS'22`
- Semantic Consistency Learning on Manifold for Source Data-Free Unsupervised Domain Adaptation (SCLM) [`paper`](https://www.sciencedirect.com/science/article/pii/S0893608022001897) `Neural Networks'22`
- Source-Free Domain Adaptation via Distribution Estimation (SFDA-DE) [`arxiv`](https://arxiv.org/abs/2204.11257) `CVPR'22`
- Variational Model Perturbation for Source-Free Domain Adaptation (VMP) [`arxiv`](https://arxiv.org/abs/2210.10378) `NeurIPS'22`
- Adaptive Adversarial Network for Source-Free Domain Adaptation (A2Net) [`paper`](https://openaccess.thecvf.com/content/ICCV2021/html/Xia_Adaptive_Adversarial_Network_for_Source-Free_Domain_Adaptation_ICCV_2021_paper.html) `ICCV'21`
- Casting a BAIT for Offline and Online Source-free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2010.12427) `CVIU'21`
- Domain Impression: A Source Data Free Domain Adaptation Method [`paper`](https://openaccess.thecvf.com/content/WACV2021/html/Kurmi_Domain_Impression_A_Source_Data_Free_Domain_Adaptation_Method_WACV_2021_paper.html) `WACV'21`
- Exploiting the Intrinsic Neighborhood Structure for Source-free Domain Adaptation (NRC) [`arxiv`](https://arxiv.org/abs/2110.04202) [`code`](https://github.com/Albert0147/NRC_SFDA) `NeurIPS'21` [![Stars](https://img.shields.io/github/stars/Albert0147/NRC_SFDA?style=social)](https://github.com/Albert0147/NRC_SFDA)
- Generalized Source-Free Domain Adaptation (G-SFDA) [`paper`](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_Generalized_Source-Free_Domain_Adaptation_ICCV_2021_paper.html) [`arxiv`](https://arxiv.org/abs/2108.01614) `ICCV'21`
- Model Adaptation through Hypothesis Transfer with Gradual Knowledge Distillation (GKD) [`paper`](https://ieeexplore.ieee.org/abstract/document/9636206) `IROS'21`
- Source Data-absent Unsupervised Domain Adaptation through Hypothesis Transfer and Labeling Transfer (SHOT++) [`paper`](https://ieeexplore.ieee.org/abstract/document/9512429) [`arxiv`](https://arxiv.org/abs/2012.07297) [`code`](https://github.com/tim-learn/SHOT-plus) `TPAMI'21` [![Stars](https://img.shields.io/github/stars/tim-learn/SHOT-plus?style=social)](https://github.com/tim-learn/SHOT-plus)
- Source-free Domain Adaptation via Avatar Prototype Generation and Adaptation (CPGA) [`arxiv`](https://arxiv.org/abs/2106.15326) `IJCAI'21`
- Do We Really Need to Access the Source Data? Source Hypothesis Transfer for Unsupervised Domain Adaptation (SHOT) [`paper`](http://proceedings.mlr.press/v119/liang20a/liang20a.pdf) [`arxiv`](https://arxiv.org/abs/2002.08546) [`code`](https://github.com/tim-learn/SHOT) `ICML'20` [![Stars](https://img.shields.io/github/stars/tim-learn/SHOT?style=social)](https://github.com/tim-learn/SHOT)
- Model Adaptation: Unsupervised Domain Adaptation Without Source Data [`paper`](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Model_Adaptation_Unsupervised_Domain_Adaptation_Without_Source_Data_CVPR_2020_paper.html) `CVPR'20`

### Object Detection
- Adapting with an Open Mind: Leveraging Open-Vocabulary Detectors for Closed Set Source-Free Domain Adaptive Object Detection (CVPR 2026 Findings) [`paper`](https://openaccess.thecvf.com/content/CVPR2026F/html/Borgavi_Adapting_with_an_Open_Mind_Leveraging_Open-Vocabulary_Detectors_for_Closed_CVPRF_2026_paper.html)
- Beyond Boundaries: Leveraging Vision Foundation Models for Source-Free Object Detection [`arxiv`](https://arxiv.org/abs/2511.07301) `AAAI'26`
- CGSA: Class-Guided Slot-Aware Adaptation for Source-Free Object Detection [`paper`](https://iclr.cc/virtual/2026/poster/10006534) [`arxiv`](https://arxiv.org/abs/2602.22621) `ICLR'26`
- Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/VCR_Foundation_Model_Priors_Enhance_Object_Focus_in_Feature_Space_for_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2512.17514) `CVPR'26`
- Real-Time Source-Free Object Detection [`arxiv`](https://arxiv.org/abs/2606.31834) `ECCV'26`
- SFDATrack: Generalized Source-Free Domain Adaptive Tracking Under Adverse Weather Conditions [`arxiv`](https://arxiv.org/abs/2607.00369) `ECCV'26`
- Towards Unbiased Source-Free Object Detection via Vision Foundation Models [`arxiv`](https://arxiv.org/abs/2601.12765) `arXiv'26`
- Context Aware Grounded Teacher for Source Free Object Detection [`arxiv`](https://arxiv.org/abs/2504.15404) [`project`](https://tajamul21.github.io/Grounded_Teacher/) `IJCV'25`
- Dual-Rate Dynamic Teacher for Source-Free Domain Adaptive Object Detection [`paper`](https://openaccess.thecvf.com/content/ICCV2025/html/He_Dual-Rate_Dynamic_Teacher_for_Source-Free_Domain_Adaptive_Object_Detection_ICCV_2025_paper.html) `ICCV'25`
- Leveraging Confident Image Regions for Source-Free Domain-Adaptive Object Detection [`arxiv`](https://arxiv.org/abs/2501.10081) `arXiv'25`
- MIAdapt: Source-free Few-shot Domain Adaptive Object Detection for Microscopic Images [`arxiv`](https://arxiv.org/abs/2503.03370) `arXiv'25`
- SFUOD: Source-Free Unknown Object Detection [`paper`](https://openaccess.thecvf.com/content/ICCV2025/html/Park_SFUOD_Source-Free_Unknown_Object_Detection_ICCV_2025_paper.html) [`arxiv`](https://arxiv.org/abs/2507.17373) `ICCV'25`
- Source-Free Object Detection with Detection Transformer [`arxiv`](https://arxiv.org/abs/2510.11090) `TIP'25`
- Simplifying Source-Free Domain Adaptation for Object Detection [`paper`](https://link.springer.com/chapter/10.1007/978-3-031-72949-2_12) [`arxiv`](https://arxiv.org/abs/2407.07586) [`code`](https://github.com/EPFL-IMOS/simple-SFOD) `ECCV'24` [![Stars](https://img.shields.io/github/stars/EPFL-IMOS/simple-SFOD?style=social)](https://github.com/EPFL-IMOS/simple-SFOD)
- Source-Free Domain Adaptation for YOLO Object Detection [`paper`](https://dl.acm.org/doi/10.1007/978-3-031-91672-4_14) [`arxiv`](https://arxiv.org/pdf/2409.16538) [`code`](https://github.com/vs-cv/sf-yolo) `ECCV'24` [![Stars](https://img.shields.io/github/stars/vs-cv/sf-yolo?style=social)](https://github.com/vs-cv/sf-yolo)
- Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection [`arxiv`](https://arxiv.org/abs/2203.15793) [`code`](https://github.com/Vibashan/irg-sfda) `CVPR'22` [![Stars](https://img.shields.io/github/stars/Vibashan/irg-sfda?style=social)](https://github.com/Vibashan/irg-sfda)
- Source-Free Object Detection by Learning To Overlook Domain Style (LODS) [`paper`](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Source-Free_Object_Detection_by_Learning_To_Overlook_Domain_Style_CVPR_2022_paper.html) `CVPR'22`

### Semantic Segmentation (2D)
- Denoise and Align: Towards Source-Free UDA for Robust Panoramic Semantic Segmentation [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Chang_Denoise_and_Align_Towards_Source-Free_UDA_for_Robust_Panoramic_Semantic_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2603.25131) `CVPR'26`
- Towards Stable Source-Free Domain Adaptive Semantic Segmentation [`paper`](https://doi.org/10.1007/s11263-026-02929-6) `IJCV'26`
- 360SFUDA++: Towards Source-Free UDA for Panoramic Segmentation by Learning Reliable Category Prototypes [`paper`](https://doi.org/10.1109/TPAMI.2024.3490619) `TPAMI'25`
- Lost in Translation? Vocabulary Alignment for Source-Free Adaptation in Open-Vocabulary Semantic Segmentation [`arxiv`](https://arxiv.org/abs/2509.15225) [`code`](https://github.com/Sisso16/VocAlign) `BMVC'25` [![Stars](https://img.shields.io/github/stars/Sisso16/VocAlign?style=social)](https://github.com/Sisso16/VocAlign)
- Supportive Negatives Spectral Augmentation for Source-Free Cross-Domain Segmentation [`paper`](https://doi.org/10.1609/aaai.v39i10.33148) `AAAI'25`
- Unlocking Constraints: Source-Free Occlusion-Aware Seamless Segmentation [`paper`](https://openaccess.thecvf.com/content/ICCV2025/html/Cao_Unlocking_Constraints_Source-Free_Occlusion-Aware_Seamless_Segmentation_ICCV_2025_paper.html) [`arxiv`](https://arxiv.org/abs/2506.21198) [`code`](https://github.com/yihong-97/UNLOCK) `ICCV'25` [![Stars](https://img.shields.io/github/stars/yihong-97/UNLOCK?style=social)](https://github.com/yihong-97/UNLOCK)
- SFDA for RGB-D Semantic Segmentation with Vision Transformers [`paper`](https://arxiv.org/abs/2305.14269) `arXiv'24`
- Stable Neighbor Denoising for Source-free Domain Adaptive Segmentation [`paper`](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_Stable_Neighbor_Denoising_for_Source-free_Domain_Adaptive_Segmentation_CVPR_2024_paper.pdf) [`arxiv`](https://arxiv.org/abs/2406.06813) [`code`](https://github.com/DZhaoXd/SND) `CVPR'24` [![Stars](https://img.shields.io/github/stars/DZhaoXd/SND?style=social)](https://github.com/DZhaoXd/SND)
- Generalize Then Adapt: Source-Free Domain Adaptive Semantic Segmentation [`paper`](https://openaccess.thecvf.com/content/ICCV2021/html/Kundu_Generalize_Then_Adapt_Source-Free_Domain_Adaptive_Semantic_Segmentation_ICCV_2021_paper.html) `ICCV'21`
- Source-Free Domain Adaptation for Semantic Segmentation [`paper`](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_Source-Free_Domain_Adaptation_for_Semantic_Segmentation_CVPR_2021_paper.html) `CVPR'21`

### Remote Sensing
- Machine Unlearning for Source-Free Unsupervised Partial-Domain Adaptation in Remote Sensing [`paper`](https://doi.org/10.1109/TGRS.2025.3637240) `TGRS'25`
- Multi-level domain perturbation for source-free object detection in remote sensing images [`paper`](https://doi.org/10.1080/10095020.2024.2378920) `Geo-spatial Information Science'25`
- Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation [`paper`](https://doi.org/10.1109/icassp55912.2026.11464091) [`arxiv`](https://arxiv.org/abs/2509.16942) `ICASSP'26`
- Source-Free Cross-Domain Scene Classification of Remote Sensing Images via Statistics Matching and Noise Adaptation [`paper`](https://doi.org/10.1109/TGRS.2025.3590697) `TGRS'25`
- Source-Free Domain Adaptation for Remote Sensing Object Detection Using Low-Confidence Pseudolabels [`paper`](https://doi.org/10.1109/LGRS.2025.3557816) `GRSL'25`
- Source-Free Domain Adaptive Semantic Segmentation of Remote Sensing Images with Diffusion-Guided Label Enrichment [`paper`](https://doi.org/10.1109/jstars.2026.3693002) [`arxiv`](https://arxiv.org/abs/2509.18502) `JSTARS'26`
- VFM-Guided Semi-Supervised Detection Transformer under Source-Free Constraints for Remote Sensing Object Detection [`paper`](https://doi.org/10.1109/jstars.2026.3689075) [`arxiv`](https://arxiv.org/abs/2508.11167) `JSTARS'26`

### Landmine Detection
- SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift [`arxiv`](https://arxiv.org/abs/2607.28996) [`dataset`](https://huggingface.co/datasets/SagarLekhak/SULAND_v2_RGB_Surface_Landmine_Dataset) [`code`](https://github.com/PrasannaPulakurthi/SULAND_v2) `arXiv'26` [![Stars](https://img.shields.io/github/stars/PrasannaPulakurthi/SULAND_v2?style=social)](https://github.com/PrasannaPulakurthi/SULAND_v2)

### 3D / Point Cloud
- Source-Free Domain Adaptation for Geospatial Point Cloud Semantic Segmentation [`arxiv`](https://arxiv.org/abs/2601.08375) `arXiv'26`
- Omni-Query Active Learning for Source-Free Domain Adaptive Cross-Modality 3D Semantic Segmentation [`paper`](https://doi.org/10.1609/aaai.v39i8.32941) `AAAI'25`
- PointSFDA: Source-free Domain Adaptation for Point Cloud Completion [`arxiv`](https://arxiv.org/abs/2503.15144) [`code`](https://github.com/Starak-x/PointSFDA) `arXiv'25` [![Stars](https://img.shields.io/github/stars/Starak-x/PointSFDA?style=social)](https://github.com/Starak-x/PointSFDA)
- Towards Stable and Robust Source-free Unsupervised 3D Semantic Segmentation [`paper`](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02968.pdf) `ECCV'24`

### Medical Imaging
- DiffuSAM: Diffusion-Based Prompt-Free SAM2 for Few-Shot and Source-Free Medical Image Segmentation [`arxiv`](https://arxiv.org/abs/2604.24719) `arXiv'26`
- Federated Spatial Prior-Based Source-Free Domain Adaptation for White Matter Hyperintensities Segmentation [`paper`](https://doi.org/10.1109/JBHI.2025.3612029) `JBHI'26`
- Forgetting-Resistant and Lesion-Aware Source-Free Domain Adaptive Fundus Image Analysis with Vision-Language Model [`arxiv`](https://arxiv.org/abs/2602.19471) `arXiv'26`
- Geometric Correspondence Constrained Pseudo-Label Alignment for Source-Free Domain Adaptive Fundus Image Segmentation [`paper`](https://doi.org/10.1609/aaai.v40i6.42502) `AAAI'26`
- Source-Free Active Domain Adaptation via Influential-Points-Guided Progressive Teacher for Medical Image Segmentation [`paper`](https://doi.org/10.1109/TMI.2025.3619837) `TMI'26`
- Versatile Source-Free Active Domain Adaptation for multi-center and multi-rater medical image segmentation [`paper`](https://doi.org/10.1016/j.inffus.2025.103586) `Information Fusion'26`
- Zero-LEAD: Source-Free Universal Domain Adaptation for Abdominal Multi-Organ Segmentation [`paper`](https://openaccess.thecvf.com/content/WACV2026/html/El-Sayed_Zero-LEAD_Source-Free_Universal_Domain_Adaptation_for_Abdominal_Multi-Organ_Segmentation_WACV_2026_paper.html) `WACV'26`
- Active Source-Free Cross-Domain and Cross-Modality Adaptation for Volumetric Medical Image Segmentation by Image Sensitivity and Organ Heterogeneity Sampling [`paper`](https://doi.org/10.1007/978-3-032-04978-0_1) `MICCAI'25`
- AIF-SFDA: Autonomous Information Filter-driven Source-Free Domain Adaptation for Medical Image Segmentation [`arxiv`](https://arxiv.org/abs/2501.03074) [`code`](https://github.com/JingHuaMan/AIF-SFDA) `AAAI'25` [![Stars](https://img.shields.io/github/stars/JingHuaMan/AIF-SFDA?style=social)](https://github.com/JingHuaMan/AIF-SFDA)
- Aligning What You Separate: Denoised Patch Mixing for Source-Free Domain Adaptation in Medical Image Segmentation [`paper`](https://doi.org/10.1109/icassp55912.2026.11463987) [`arxiv`](https://arxiv.org/abs/2510.25227) `ICASSP'26`
- Continual source-free active domain adaptation for nasopharyngeal carcinoma tumor segmentation across multiple hospitals [`paper`](https://doi.org/10.1016/j.neunet.2025.107869) `Neural Networks'25`
- DDFP: Data-dependent Frequency Prompt for Source Free Domain Adaptation of Medical Image Segmentation [`arxiv`](https://arxiv.org/abs/2505.09927) `arXiv'25`
- Dual Knowledge-Aware Guidance for Source-Free Domain Adaptive Fundus Image Segmentation [`paper`](https://doi.org/10.1007/978-3-032-04978-0_18) `MICCAI'25`
- GrInAdapt: Source-Free Multi-target Domain Adaptation for Retinal Vessel Segmentation [`paper`](https://doi.org/10.1007/978-3-032-04971-1_21) [`arxiv`](https://arxiv.org/abs/2503.05991) `MICCAI'25`
- HEAL: Learning-Free Source Free Unsupervised Domain Adaptation for Cross-Modality Medical Image Segmentation [`arxiv`](https://arxiv.org/abs/2511.17958) `BMVC'25`
- Leveraging Segment Anything Model for Source-Free Domain Adaptation via Dual Feature Guided Auto-Prompting [`arxiv`](https://arxiv.org/abs/2505.08527) `TMI'25`
- ProSFDA: Source-free Domain Adaptation Using Prompt Learning for Medical Image Segmentation [`paper`](https://doi.org/10.1016/j.patcog.2025.112290) [`code`](https://github.com/ShishuaiHu/ProSFDA) `Pattern Recognition'25` [![Stars](https://img.shields.io/github/stars/ShishuaiHu/ProSFDA?style=social)](https://github.com/ShishuaiHu/ProSFDA)
- Source-Free Active Domain Adaptation for Efficient Medical Video Polyp Segmentation [`paper`](https://doi.org/10.1007/978-3-032-05127-1_48) `MICCAI'25`
- Source-Free Domain Adaptation for Cross-Modality Cardiac Image Segmentation with Contrastive Class Relationship Consistency [`paper`](https://doi.org/10.1007/978-3-032-04971-1_54) `MICCAI'25`
- SRPL-SFDA: SAM-Guided Reliable Pseudo-Labels for Source-Free Domain Adaptation in Medical Image Segmentation [`arxiv`](https://arxiv.org/abs/2506.09403) `Neurocomputing'25`
- VP-SFDA: Visual Prompt Source-Free Domain Adaptation for Cross-Modal Medical Image Segmentation [`paper`](https://spj.science.org/doi/10.34133/hds.0143) `Health Data Science'25`
- Reliable Source Approximation: Source-Free Unsupervised Domain Adaptation for Vestibular Schwannoma MRI Segmentation [`arxiv`](https://arxiv.org/abs/2405.16102) `MICCAI'24`
- Robust Source-Free Domain Adaptation for Fundus Image Segmentation [`paper`](https://openaccess.thecvf.com/content/WACV2024/papers/Li_Robust_Source-Free_Domain_Adaptation_for_Fundus_Image_Segmentation_WACV_2024_paper.pdf) [`code`](https://github.com/LinGrayy/PLPB) `WACV'24` [![Stars](https://img.shields.io/github/stars/LinGrayy/PLPB?style=social)](https://github.com/LinGrayy/PLPB)

### Video / Action Recognition
- Co-STAR: Collaborative Curriculum Self-Training with Adaptive Regularization for Source-Free Video Domain Adaptation [`paper`](https://doi.org/10.1109/WACV61042.2026.00755) [`arxiv`](https://arxiv.org/abs/2504.11669) `WACV'26`
- Source-free Video Domain Adaptation by Learning from Noisy Labels [`paper`](https://www.sciencedirect.com/science/article/abs/pii/S0031320324010793) [`code`](https://github.com/avijit9/CleanAdapt) `Pattern Recognition'25` [![Stars](https://img.shields.io/github/stars/avijit9/CleanAdapt?style=social)](https://github.com/avijit9/CleanAdapt)
- Source-Free Video Domain Adaptation With Spatial-Temporal-Historical Consistency Learning [`paper`](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Source-Free_Video_Domain_Adaptation_With_Spatial-Temporal-Historical_Consistency_Learning_CVPR_2023_paper.html) `CVPR'23`
- Source-free Video Domain Adaptation by Learning Temporal Consistency for Action Recognition (ATCoN) [`arxiv`](https://arxiv.org/abs/2203.04559) [`code`](https://github.com/xuyu0010/ATCoN) `ECCV'22` [![Stars](https://img.shields.io/github/stars/xuyu0010/ATCoN?style=social)](https://github.com/xuyu0010/ATCoN)

### Person Re-Identification
- AIDA-ReID: Adaptive Intermediate Domain Adaptation for Generalizable and Source-Free Person Re-Identification [`arxiv`](https://arxiv.org/abs/2605.00111) `arXiv'26`
- Learning Source-Free Domain Adaptation for Visible-Infrared Person Re-Identification [`paper`](https://papers.nips.cc/paper_files/paper/2025/hash/1d6dfe3f64546be88741e05302e42860-Abstract-Conference.html) `NeurIPS'25`
- RULER: Source-free Domain Adaptive Person Re-identification via Uncertain Label Refinery [`paper`](https://doi.org/10.1007/s11633-025-1543-7) `Machine Intelligence Research'25`
- SecureDA: Privacy-Preserving Source-Free Domain Adaptation for Person Re-Identification [`paper`](https://doi.org/10.1109/TMM.2025.3599094) `TMM'25`

### Face Anti-Spoofing
- Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing [`paper`](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimal_Transport-Guided_Source-Free_Adaptation_for_Face_Anti-Spoofing_CVPR_2025_paper.html) [`arxiv`](https://arxiv.org/abs/2503.22984) `CVPR'25`
- Source-Free Domain Adaptation With Domain Generalized Pretraining for Face Anti-Spoofing [`paper`](https://doi.org/10.1109/TPAMI.2024.3370721) `TPAMI'24`
- Source-Free Domain Adaptation with Contrastive Domain Alignment and Self-supervised Exploration for Face Anti-spoofing [`paper`](https://link.springer.com/chapter/10.1007/978-3-031-19775-8_30) `ECCV'22`

### Facial Expression / Emotion Recognition
- Fuzzy-Aware Loss for Source-Free Domain Adaptation in Visual Emotion Recognition [`arxiv`](https://arxiv.org/abs/2501.15519) `IEEE Transactions on Fuzzy Systems'26`
- Personalized Feature Translation for Expression Recognition: An Efficient Source-Free Domain Adaptation Method [`paper`](https://iclr.cc/virtual/2026/poster/10011889) [`arxiv`](https://arxiv.org/abs/2508.09202) `ICLR'26`
- Disentangled Source-Free Personalization for Facial Expression Recognition with Neutral Target Data [`arxiv`](https://arxiv.org/abs/2503.20771) `FG'25`
- Bridge then Begin Anew: Generating Target-relevant Intermediate Model for Source-free Visual Emotion Adaptation [`arxiv`](https://arxiv.org/abs/2412.13577) `AAAI'25`

### Human Pose Estimation
- Lifelong Domain Adaptive 3D Human Pose Estimation [`arxiv`](https://arxiv.org/abs/2512.23860) `AAAI'26`
- Prior-guided Source-free Domain Adaptation for Human Pose Estimation [`paper`](https://openaccess.thecvf.com/content/ICCV2023/html/Raychaudhuri_Prior-guided_Source-free_Domain_Adaptation_for_Human_Pose_Estimation_ICCV_2023_paper.html) `ICCV'23`

### Image Super-Resolution
- Uncertainty-Aware Source-Free Adaptive Image Super-Resolution with Wavelet Augmentation Transformer [`paper`](https://openaccess.thecvf.com/content/CVPR2024/papers/Ai_Uncertainty-Aware_Source-Free_Adaptive_Image_Super-Resolution_with_Wavelet_Augmentation_Transformer_CVPR_2024_paper.pdf) [`arxiv`](https://arxiv.org/abs/2303.17783) [`code`](https://github.com/shallowdream204/SODA-SR) `CVPR'24` [![Stars](https://img.shields.io/github/stars/shallowdream204/SODA-SR?style=social)](https://github.com/shallowdream204/SODA-SR)

### Time Series & Signals
- Evidentially Calibrated Source-Free Time-Series Domain Adaptation With Temporal Imputation [`paper`](https://doi.org/10.1109/TKDE.2025.3621774) `TKDE'26`
- Position regularization-based temporal-spectral imputation for source-free time-series domain adaptation [`paper`](https://doi.org/10.1016/j.neucom.2025.131981) `Neurocomputing'26`
- Source-Free Domain Adaptation with complex distribution considerations for time series data [`paper`](https://doi.org/10.1016/j.datak.2025.102501) `Data & Knowledge Engineering'26`
- Source-free time series domain adaptation with class-aware temporal imputation [`paper`](https://doi.org/10.1016/j.ipm.2026.104658) `Information Processing & Management'26`
- Source-Free Time-Series Domain Adaptation With Prior Evaluation of Model Salience [`paper`](https://doi.org/10.1109/TNNLS.2025.3641830) `TNNLS'26`
- Temporal Source Recovery for Time-Series Source-Free Unsupervised Domain Adaptation [`paper`](https://doi.org/10.1109/TPAMI.2026.3681762) [`arxiv`](https://arxiv.org/abs/2409.19635) `TPAMI'26`
- Classifier ensemble based source-free domain adaptation for time series classification [`paper`](https://doi.org/10.1016/j.knosys.2025.114584) `Knowledge-Based Systems'25`
- Learning Compositional Transferability of Time Series for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2504.14994) `arXiv'25`
- Source-free time series domain adaptation with wavelet-based multi-scale temporal imputation [`paper`](https://doi.org/10.1016/j.neunet.2025.107428) `Neural Networks'25`
- Temporal Restoration and Spatial Rewiring for Source-Free Multivariate Time Series Domain Adaptation [`paper`](https://doi.org/10.1145/3711896.3737150) [`arxiv`](https://arxiv.org/abs/2505.21525) `KDD'25`
- Time and frequency synergy for source-free time-series domain adaptations [`paper`](https://doi.org/10.1016/j.ins.2024.121734) `Information Sciences'25`

## Settings & Extensions

### Test-Time Adaptation (TTA)
- Test-Time Adaptation by Causal Trimming [`arxiv`](https://arxiv.org/abs/2510.11133) [`code`](https://github.com/NancyQuris/TACT) `NeurIPS'25` [![Stars](https://img.shields.io/github/stars/NancyQuris/TACT?style=social)](https://github.com/NancyQuris/TACT)
- Backpropagation-Free Test-Time Adaptation via Probabilistic Gaussian Alignment [`paper`](https://neurips.cc/virtual/2025/poster/115767) [`code`](https://github.com/AIM-SKKU/ADAPT) `NeurIPS'25` [![Stars](https://img.shields.io/github/stars/AIM-SKKU/ADAPT?style=social)](https://github.com/AIM-SKKU/ADAPT)
- Cross-Device Collaborative Test-Time Adaptation [`paper`](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0e668df3fe63ec89e5a7e68f3d350f-Paper-Conference.pdf) [`code`](https://github.com/Cascol-Chen/COLA) `NeurIPS'24` [![Stars](https://img.shields.io/github/stars/Cascol-Chen/COLA?style=social)](https://github.com/Cascol-Chen/COLA)
- PCoTTA: Continual Test-Time Adaptation for Multi-Task Point Cloud Understanding [`arxiv`](https://arxiv.org/abs/2411.00632) [`code`](https://github.com/Jinec98/PCoTTA) `NeurIPS'24` [![Stars](https://img.shields.io/github/stars/Jinec98/PCoTTA?style=social)](https://github.com/Jinec98/PCoTTA)
- L-TTA: Lightweight Test-Time Adaptation Using a Versatile Stem Layer [`paper`](https://proceedings.neurips.cc/paper_files/paper/2024/file/458d9f2dd5c7565af60143630dc62f10-Paper-Conference.pdf) `NeurIPS'24`
- Protected Test-Time Adaptation via Online Entropy Matching: A Betting Approach [`paper`](https://neurips.cc/virtual/2024/poster/93486) `NeurIPS'24`
- Discriminator-Guided Adaptive Diffusion for Source-Free Test-Time Adaptation under Image Corruptions [`arxiv`](https://arxiv.org/abs/2604.23636) `ICPR'26`
- Distill Once, Adapt Life-Long: Exploring Dataset Distillation for Continual Test-Time Adaptation [`arxiv`](https://arxiv.org/abs/2606.20196) `ECCV'26`
- Source-Free Controlled Adaptation of Teachers for Continual Test-Time Adaptation [`arxiv`](https://arxiv.org/abs/2607.23735) `arXiv'26`
- TestMate: Test-Time Domain Adaptation Aided by Lightweight Vision Foundation Model [`arxiv`](https://arxiv.org/abs/2607.03810) `arXiv'26`
- Purge-Gate: Backpropagation-Free Test-Time Adaptation for Point Clouds Classification via Token Purging [`paper`](https://doi.org/10.1109/iccv51701.2025.02566) [`arxiv`](https://arxiv.org/abs/2509.09785) `ICCV'25`
- SloMo-Fast: Slow-Momentum and Fast-Adaptive Teachers for Source-Free Continual Test-Time Adaptation [`arxiv`](https://arxiv.org/abs/2511.18468) `arXiv'25`
- EcoTTA: Memory-Efficient Continual Test-Time Adaptation via Self-Distilled Regularization [`paper`](https://openaccess.thecvf.com/content/CVPR2023/html/Song_EcoTTA_Memory-Efficient_Continual_Test-Time_Adaptation_via_Self-Distilled_Regularization_CVPR_2023_paper.html) `CVPR'23`
- Towards Stable Test-Time Adaptation in Dynamic Wild World (SAR) [`arxiv`](https://arxiv.org/abs/2302.12400) `ICLR'23`
- DELTA: Degradation-Free Fully Test-Time Adaptation [`arxiv`](https://arxiv.org/abs/2301.13018) `ICLR'23`
- Contrastive Test-Time Adaptation (AdaContrast) [`paper`](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_Contrastive_Test-Time_Adaptation_CVPR_2022_paper.html) [`code`](https://github.com/DianCh/AdaContrast) `CVPR'22` [![Stars](https://img.shields.io/github/stars/DianCh/AdaContrast?style=social)](https://github.com/DianCh/AdaContrast)
- Continual Test-Time Domain Adaptation (CoTTA) [`paper`](https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Continual_Test-Time_Domain_Adaptation_CVPR_2022_paper.html) [`code`](https://github.com/qinenergy/cotta) `CVPR'22` [![Stars](https://img.shields.io/github/stars/qinenergy/cotta?style=social)](https://github.com/qinenergy/cotta)
- Efficient Test-Time Model Adaptation without Forgetting (EATA) [`paper`](https://proceedings.mlr.press/v162/niu22a.html) [`code`](https://github.com/mr-eggplant/EATA) `ICML'22` [![Stars](https://img.shields.io/github/stars/mr-eggplant/EATA?style=social)](https://github.com/mr-eggplant/EATA)
- MEMO: Test Time Robustness via Adaptation and Augmentation [`arxiv`](https://arxiv.org/abs/2110.09506) `NeurIPS'22`
- NOTE: Robust Continual Test-time Adaptation Against Temporal Correlation [`arxiv`](https://arxiv.org/abs/2208.05117) `NeurIPS'22`
- Tent: Fully Test-Time Adaptation by Entropy Minimization [`arxiv`](https://arxiv.org/abs/2006.10726) `ICLR'21`

### Open-Set / Class Distribution Shift
- Beyond Retraining: Training-Free Unknown Class Filtering for Source-Free Open Set Domain Adaptation of Vision-Language Models [`paper`](https://doi.org/10.1609/aaai.v40i28.39495) [`arxiv`](https://arxiv.org/abs/2504.14224) `AAAI'26`
- Exploring Generic Knowledge and Reactivating Source Model for Source-Free Universal Domain Adaptation [`paper`](https://doi.org/10.1109/TMM.2026.3651024) `TMM'26`
- LFM: Leveraging Foundation Models for Source-Free Universal Domain Adaptation [`arxiv`](https://arxiv.org/abs/2607.17653) `TMM'26`
- Uncertainty-guided Open-Set Source-Free Unsupervised Domain Adaptation with Target-private Class Segregation [`paper`](https://doi.org/10.1007/s11263-025-02683-1) `IJCV'26`
- Active source-free open-set domain adaptation [`paper`](https://doi.org/10.1016/j.knosys.2025.114342) `Knowledge-Based Systems'25`
- Analysis of Pseudo-Labeling for Online Source-Free Universal Domain Adaptation [`arxiv`](https://arxiv.org/abs/2504.11992) `EUSIPCO'25`
- Distinguish Then Exploit: Source-free Open Set Domain Adaptation via Weight Barcode Estimation and Sparse Label Assignment [`paper`](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.html) [`pdf`](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.pdf) `CVPR'25`
- Recall and Refine: A Simple but Effective Source-free Open-set Domain Adaptation Framework [`arxiv`](https://arxiv.org/abs/2411.12558) `TMLR'25`
- Robust Nearest Neighbors for Source-Free Domain Adaptation under Class Distribution Shift [`paper`](https://eccv.ecva.net/virtual/2024/poster/833) [`code`](https://github.com/CyberAgentAILab/Robust_Nearest_Neighbors_SFDA-CDS) `ECCV'24` [![Stars](https://img.shields.io/github/stars/CyberAgentAILab/Robust_Nearest_Neighbors_SFDA-CDS?style=social)](https://github.com/CyberAgentAILab/Robust_Nearest_Neighbors_SFDA-CDS)
- Unveiling the Unknown: Unleashing the Power of Unknown to Known in Open-Set Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/CVPR2024/papers/Wan_Unveiling_the_Unknown_Unleashing_the_Power_of_Unknown_to_Known_CVPR_2024_paper.pdf) [`code`](https://github.com/xdwfl/UPUK) `CVPR'24` [![Stars](https://img.shields.io/github/stars/xdwfl/UPUK?style=social)](https://github.com/xdwfl/UPUK)
- Universal Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content_CVPR_2020/html/Kundu_Universal_Source-Free_Domain_Adaptation_CVPR_2020_paper.html) `CVPR'20`

### Continual / Class-Incremental SFDA
- GMM-COMET: Continual Source-Free Universal Domain Adaptation via a Mean Teacher and Gaussian Mixture Model-Based Pseudo-Labeling [`arxiv`](https://arxiv.org/abs/2601.11161) `arXiv'26`
- SCoDA: Self-supervised Continual Domain Adaptation [`paper`](https://doi.org/10.1145/3774521.3774553) [`arxiv`](https://arxiv.org/abs/2509.09935) `ICVGIP'25`
- Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Multi-Granularity_Class_Prototype_Topology_Distillation_for_Class-Incremental_Source-Free_Unsupervised_Domain_CVPR_2025_paper.html) [`arxiv`](https://arxiv.org/abs/2411.16064) `CVPR'25`
- CoSDA: Continual Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2304.06627) `ICLR'23`

### Multi-Source SFDA
- Agile Multi-Source-Free Domain Adaptation [`paper`](https://ojs.aaai.org/index.php/AAAI/article/view/29272) `AAAI'24`
- Selection, Ensemble, and Adaptation: Advancing Multi-Source-Free Domain Adaptation via Architecture Zoo [`paper`](https://doi.org/10.1109/TPAMI.2025.3593943) `TPAMI'25`
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization [`paper`](https://arxiv.org/abs/2402.08249) `arXiv'24`
- Discriminability and Transferability Estimation: A Bayesian Source Importance Estimation Approach for Multi-Source-Free Domain Adaptation [`paper`](https://doi.org/10.1609/aaai.v37i6.25946) `AAAI'23`
- Misalignment-Free Relation Aggregation for Multi-Source-Free Domain Adaptation [`paper`](https://doi.org/10.1109/ICCVW60793.2023.00466) `ICCV Workshops'23`
- Unsupervised Multi-Source Domain Adaptation Without Access to Source Data [`paper`](https://openaccess.thecvf.com/content/CVPR2021/html/Ahmed_Unsupervised_Multi-Source_Domain_Adaptation_Without_Access_to_Source_Data_CVPR_2021_paper.html) `CVPR'21`

### Federated SFDA
- FedSCAl: Leveraging Server and Client Alignment for Unsupervised Federated Source-Free Domain Adaptation [`paper`](https://doi.org/10.1109/WACV61042.2026.00400) [`arxiv`](https://arxiv.org/abs/2512.06738) `WACV'26`
- Source-free domain adaptation for cross-domain remaining useful life prediction: A distributed federated learning perspective [`paper`](https://doi.org/10.1016/j.ress.2026.112271) `Reliability Engineering & System Safety'26`
- Fed-SMTDA: A Novel Framework for Federated Source-Free Multi-Target Domain Adaptation Using Feature Clustering and Adaptive Aggregation [`paper`](https://doi.org/10.1109/IJCNN64981.2025.11227772) `IJCNN'25`
- Federated Hallucination Translation and Source-Free Regularization Adaptation in Decentralized Domain Adaptation for Foggy Scene Understanding [`paper`](https://doi.org/10.1109/TMM.2024.3521711) `TMM'25`
- Federated Source-Free Domain Adaptation for Classification: Weighted Cluster Aggregation for Unlabeled Data [`paper`](https://openaccess.thecvf.com/content/WACV2025/papers/Mori_Federated_Source-Free_Domain_Adaptation_for_Classification_Weighted_Cluster_Aggregation_for_WACV_2025_paper.pdf) `WACV'25`
- Rethinking the Backbone in Class Imbalanced Federated Source Free Domain Adaptation: The Utility of Vision Foundation Models [`paper`](https://doi.org/10.1109/ICIPW68931.2025.11386111) [`arxiv`](https://arxiv.org/abs/2509.08372) `ICIP Workshops'25`
- When Cars Meet Drones: Hyperbolic Federated Learning for Source-Free Domain Adaptation in Adverse Weather [`paper`](https://doi.org/10.1109/WACV61041.2025.00162) `WACV'25`
- Learning Across Domains and Devices: Style-Driven Source-Free Domain Adaptation in Clustered Federated Learning [`arxiv`](https://arxiv.org/abs/2210.02326) `WACV'23`

### Active SFDA
- Energy-guided active source-free domain adaptation [`paper`](https://doi.org/10.1007/s11042-026-21692-x) `Multimedia Tools and Applications'26`
- Active source-free domain adaptation for intracranial EEG classification via neighborhood uncertainty and diversity [`paper`](https://doi.org/10.1016/j.bspc.2024.107464) `Biomedical Signal Processing and Control'25`
- DAM: Dual Active Learning with Multimodal Foundation Model for Source-Free Domain Adaptation [`paper`](https://doi.org/10.1109/icassp55912.2026.11463823) [`arxiv`](https://arxiv.org/abs/2509.24896) `ICASSP'26`
- Propensity-driven Uncertainty Learning for Sample Exploration in Source-Free Active Domain Adaptation [`arxiv`](https://arxiv.org/abs/2501.13517) `arXiv'25`
- Source-Free Active Domain Adaptation via Augmentation-Based Sample Query and Progressive Model Adaptation [`paper`](https://doi.org/10.1109/TNNLS.2023.3338294) `TNNLS'25`
- Structure-Based Uncertainty Estimation for Source-Free Active Domain Adaptation [`paper`](https://doi.org/10.1049/cvi2.70020) `IET Computer Vision'25`

### Cross-Domain Few-Shot
- Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Yi_Addressing_Exacerbated_Attention_Sink_for_Source-Free_Cross-Domain_Few-Shot_Learning_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2605.25799) `CVPR'26`
- Domain knowledge adaptive normalization for source-free cross-domain few-shot learning [`paper`](https://doi.org/10.1016/j.dsp.2026.106191) `Digital Signal Processing'26`
- Improving CLIP Adaptation by Breaking Tail Alignment for Source-Free Cross-Domain Few-Shot Learning [`arxiv`](https://arxiv.org/abs/2605.29776) `arXiv'26`
- Mind the Discriminability Trap in Source-Free Cross-domain Few-shot Learning [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Mind_the_Discriminability_Trap_in_Source-Free_Cross-domain_Few-shot_Learning_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2603.13341) `CVPR'26`
- Reclaiming Lost Text Layers for Source-Free Cross-Domain Few-Shot Learning [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Reclaiming_Lost_Text_Layers_for_Source-Free_Cross-Domain_Few-Shot_Learning_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2603.05235) `CVPR'26`
- Reviving In-domain Fine-tuning Methods for Source-Free Cross-domain Few-shot Learning [`arxiv`](https://arxiv.org/abs/2605.11659) `arXiv'26`
- SeGDP: Source-free Cross-domain Few-shot Learning via Semantic Guided Diversity Prompting [`paper`](https://doi.org/10.1145/3796719) `TOMM'26`
- Step-Wise Distribution-Aligned Style Prompt Tuning for Source-Free Cross-Domain Few-Shot Learning [`paper`](https://doi.org/10.1109/TPAMI.2025.3610039) [`arxiv`](https://arxiv.org/abs/2411.10070) `TPAMI'26`
- When Semantics Saturate or Emerge: Adaptation-Conditional Semantic Utility in Source-Free Cross-Domain Few-Shot Learning [`arxiv`](https://arxiv.org/abs/2608.06673) `arXiv'26`
- Asymmetric Co-Training for Source-Free Few-Shot Domain Adaptation [`arxiv`](https://arxiv.org/abs/2502.14214) `arXiv'25`
- Textual and Visual Guided Task Adaptation for Source-Free Cross-Domain Few-Shot Segmentation [`paper`](https://doi.org/10.1145/3746027.3755772) [`arxiv`](https://arxiv.org/abs/2508.05213) `ACM MM'25`
- Prompt as Free Lunch: Enhancing Diversity in Source-Free Cross-domain Few-shot Learning through Semantic-Guided Prompting [`arxiv`](https://arxiv.org/abs/2412.00767) `arXiv'24`

### Cross-Modal SFDA
- Test-Time Selective Adaptation for Uni-Modal Distribution Shift in Multi-Modal Data [`paper`](https://icml.cc/virtual/2025/poster/46389) [`code`](https://github.com/chenmc1996/Uni-Modal-Distribution-Shift) `ICML'25` [![Stars](https://img.shields.io/github/stars/chenmc1996/Uni-Modal-Distribution-Shift?style=social)](https://github.com/chenmc1996/Uni-Modal-Distribution-Shift)
- EventDance: Unsupervised Source-free Cross-modal Adaptation for Event-based Object Recognition [`paper`](https://openaccess.thecvf.com/content/CVPR2024/papers/Zheng_EventDance_Unsupervised_Source-free_Cross-modal_Adaptation_for_Event-based_Object_Recognition_CVPR_2024_paper.pdf) [`code`](https://github.com/zhengxujosh/EventDance) `CVPR'24` [![Stars](https://img.shields.io/github/stars/zhengxujosh/EventDance?style=social)](https://github.com/zhengxujosh/EventDance)

### Foundation Models / VLM-based
- Training-Free Test-Time Adaptation via Shape and Style Guidance for Vision-Language Models [`paper`](https://papers.nips.cc/paper_files/paper/2025/hash/e07ad202df8672e3cf9d0203d86f5a55-Abstract-Conference.html) `NeurIPS'25`
- Towards Dynamic-Prompting Collaboration for Source-Free Domain Adaptation [`paper`](https://doi.org/10.24963/ijcai.2024/182) `IJCAI'24`
- Closing the Confusion Loop: CLIP-Guided Alignment for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2602.08730) `arXiv'26`
- Data-Efficient CLIP-Powered Dual-Branch Networks for Source-Free Unsupervised Domain Adaptation [`arxiv`](https://arxiv.org/abs/2410.15811) `Expert Systems with Applications'26`
- Empowering Source-Free Domain Adaptation via MLLM-Guided Reliability-Based Curriculum Learning [`paper`](https://doi.org/10.1109/WACV61042.2026.00415) `WACV'26`
- Rethinking the Need for Source Models: Source-Free Domain Adaptation from Scratch Guided by a Vision-Language Model [`arxiv`](https://arxiv.org/abs/2605.02604) `arXiv'26`
- Source-Free Domain Adaptation with Vision-Language Prior [`arxiv`](https://arxiv.org/abs/2604.17748) `arXiv'26`
- Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Tell2Adapt_A_Unified_Framework_for_Source_Free_Unsupervised_Domain_Adaptation_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2603.05012) `CVPR'26`
- Vision-Language Model Guided Source-Free Domain Adaptation via Optimal Transport [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Vision-Language_Model_Guided_Source-Free_Domain_Adaptation_via_Optimal_Transport_CVPR_2026_paper.html) `CVPR'26`
- Collaborative Learning with Multiple Foundation Models for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2511.19147) `arXiv'25`
- ViLAaD: Enhancing "Attracting and Dispersing" Source-Free Domain Adaptation with Vision-and-Language Model [`arxiv`](https://arxiv.org/abs/2503.23529) `arXiv'25`
- Source-Free Domain Adaptation Guided by Vision and Vision-Language Pre-training [`paper`](https://link.springer.com/article/10.1007/s11263-024-02215-3) `IJCV'24`
- Source-Free Domain Adaptation with Frozen Multimodal Foundation Model [`paper`](https://openaccess.thecvf.com/content/CVPR2024/papers/Tang_Source-Free_Domain_Adaptation_with_Frozen_Multimodal_Foundation_Model_CVPR_2024_paper.pdf) [`arxiv`](https://arxiv.org/abs/2311.16510) [`code`](https://github.com/tntek/source-free-domain-adaptation) `CVPR'24` [![Stars](https://img.shields.io/github/stars/tntek/source-free-domain-adaptation?style=social)](https://github.com/tntek/source-free-domain-adaptation)
- ReCLIP: Refine Contrastive Language Image Pre-Training with SFDA [`paper`](https://openaccess.thecvf.com/content/WACV2024/papers/Hu_ReCLIP_Refine_Contrastive_Language_Image_Pre-Training_With_Source_Free_Domain_WACV_2024_paper.pdf) [`arxiv`](https://arxiv.org/abs/2308.03793) [`code`](https://github.com/michiganleon/ReCLIP_WACV) `WACV'24` [![Stars](https://img.shields.io/github/stars/michiganleon/ReCLIP_WACV?style=social)](https://github.com/michiganleon/ReCLIP_WACV)

### Noisy Labels in SFDA
- NRFP: A Noise-Robust Feature Plugin for Source-Free Domain Adaptation (CVPR 2026 Findings) [`paper`](https://openaccess.thecvf.com/content/CVPR2026F/html/Zou_NRFP_A_Noise-Robust_Feature_Plugin_for_Source-Free_Domain_Adaptation_CVPRF_2026_paper.html)
- DRIVE: Dual-Robustness via Information Variability and Entropic Consistency in Source-Free Unsupervised Domain Adaptation [`arxiv`](https://arxiv.org/abs/2411.15976) `arXiv'25`
- ElimPCL: Eliminating Noise Accumulation with Progressive Curriculum Labeling for Source-Free Domain Adaptation [`arxiv`](https://arxiv.org/abs/2503.23712) `ICME'25`
- De-Confusing Pseudo-Labels in Source-Free Domain Adaptation [`paper`](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10138.pdf) [`arxiv`](https://arxiv.org/abs/2401.01650) [`code`](https://github.com/ssi-research/DCPL_SFDA) `ECCV'24` [![Stars](https://img.shields.io/github/stars/ssi-research/DCPL_SFDA?style=social)](https://github.com/ssi-research/DCPL_SFDA)
- When Source-Free Domain Adaptation Meets Learning with Noisy Labels [`arxiv`](https://arxiv.org/abs/2301.13381) [`code`](https://github.com/liyi01827/SFDA_LLN) `ICLR'23` [![Stars](https://img.shields.io/github/stars/liyi01827/SFDA_LLN?style=social)](https://github.com/liyi01827/SFDA_LLN)

### Security / Privacy
- ⊘ Source Models Leak What They Shouldn't ↛: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization [`paper`](https://openaccess.thecvf.com/content/CVPR2026/html/Devalapally_oslash_Source_Models_Leak_What_They_Shouldnt_nrightarrow_Unlearning_Zero-Shot_CVPR_2026_paper.html) [`arxiv`](https://arxiv.org/abs/2604.08238) `CVPR'26`
- Vicinity-Guided Discriminative Latent Diffusion for Privacy-Preserving Domain Adaptation [`paper`](https://papers.nips.cc/paper_files/paper/2025/hash/d7152995e5e9ab9ce7dccee054f03dc0-Abstract-Conference.html) [`arxiv`](https://arxiv.org/abs/2510.00478) `NeurIPS'25`
- AdaptGuard: Defending Against Universal Attacks for Model Adaptation [`arxiv`](https://arxiv.org/abs/2303.10594) `ICCV'23`
- SSDA: Secure Source-Free Domain Adaptation [`paper`](https://openaccess.thecvf.com/content/ICCV2023/html/Ahmed_SSDA_Secure_Source-Free_Domain_Adaptation_ICCV_2023_paper.html) [`code`](https://github.com/ML-Security-Research-LAB/SSDA) `ICCV'23` [![Stars](https://img.shields.io/github/stars/ML-Security-Research-LAB/SSDA?style=social)](https://github.com/ML-Security-Research-LAB/SSDA)

## Datasets & Benchmarks

Before comparing any two published numbers, check that they were produced the
same way. Most apparent contradictions in this literature come from protocol
differences rather than from method quality.

**Backbone matters more than the method, often.** Office-31 and Office-Home
results are usually ResNet-50, VisDA-C usually ResNet-101, and a paper switching
to a ViT or a CLIP initialisation will beat the field on backbone alone. Check
what was used before attributing a gain to the adaptation.

**VisDA-C is reported as per-class mean, not overall accuracy.** The classes are
heavily imbalanced, so the two differ by several points. Papers occasionally
report overall and the number looks anomalously high.

**Office-31 is saturated.** Reported averages sit near the ceiling and the
spread between methods is comparable to seed variance. Treat it as a sanity
check rather than evidence of an advance.

**DomainNet has two versions.** The full release contains substantial label
noise; most work uses the cleaned subset, and some use only a 4-domain or
7-task subset of it. A DomainNet number without the variant stated is not
comparable to anything.

**Source-free and source-available numbers are not interchangeable.** SFDA
methods start from a model trained on source data and never see it again; UDA
methods see both domains. Tables mixing the two exist, and the comparison
flatters whichever side had more information.

### Image Classification

| Dataset | Classes | Domains | Standard protocol |
|---|---|---|---|
| [Office-31](https://drive.google.com/file/d/0B4IapRTv9pJ1WGZVd1VDMmhwdlE/view?resourcekey=0-gNMHVtZfRAyO_t2_WrOunA) | 31 | 3 — Amazon, DSLR, Webcam | All 6 ordered pairs, averaged. ResNet-50. Saturated. |
| [Office-Home](https://www.hemanthdv.org/officeHomeDataset.html) | 65 | 4 — Art, Clipart, Product, Real World | All 12 ordered pairs, averaged. ResNet-50. The current default. |
| [VisDA-C](https://github.com/VisionLearningGroup/taskcv-2017-public/tree/master/classification) | 12 | synthetic → real | Single direction. ResNet-101. **Per-class mean**, not overall. |
| [DomainNet](http://ai.bu.edu/M3SDA/) | 345 | 6 — Clipart, Infograph, Painting, Quickdraw, Real, Sketch | Cleaned subset; state which domains and tasks. Hardest of the four. |
| [PACS](https://domaingeneralization.github.io/) | 7 | 4 — Photo, Art, Cartoon, Sketch | Leave-one-domain-out. More common in domain generalization than SFDA. |
| [Digits](http://yann.lecun.com/exdb/mnist/) | 10 | MNIST, USPS, SVHN | Usually 3 directions. Small, and largely superseded. |

### Robustness / Distribution Shift
- [ImageNet-C](https://github.com/hendrycks/robustness) — 15 corruption types at 5 severity levels
- [ImageNet-A](https://github.com/hendrycks/natural-adv-examples) — natural adversarial examples
- [ImageNet-R](https://github.com/hendrycks/imagenet-r) — renditions (art, cartoons, sculptures, etc.)
- [ImageNet-V2](https://huggingface.co/datasets/vaishaal/ImageNetV2/tree/main) — new test set with distribution shift
- [ImageNet-Sketch](https://github.com/HaohanWang/ImageNet-Sketch) — sketch renditions of ImageNet classes

### Semantic Segmentation
- [Cityscapes](https://www.cityscapes-dataset.com/) — 5000 fine-annotated urban driving frames, 30 classes
- [GTA5](https://download.visinf.tu-darmstadt.de/data/from_games/) — 24,966 synthetic frames from Grand Theft Auto V
- [SYNTHIA](https://synthia-dataset.net/) — synthetic urban scenes, 13 classes, multiple seasons/weather

### Object Detection
- [Foggy Cityscapes](https://www.cityscapes-dataset.com/) — Cityscapes with simulated fog (clear → foggy adaptation)
- [Sim10k](https://fcav.engin.umich.edu/projects/driving-in-the-matrix) — 10,000 synthetic images from Grand Theft Auto V
- [KITTI](https://www.cvlibs.net/datasets/kitti/) — autonomous driving benchmark (stereo, flow, detection, segmentation)
- [Clipart / Watercolor / Comic](https://naoto0804.github.io/cross_domain_detection/) — cross-domain detection from VOC to artistic styles

### Landmine Detection
- [SULAND v2](https://huggingface.co/datasets/SagarLekhak/SULAND_v2_RGB_Surface_Landmine_Dataset) — 33,771 RGB UAV/UGV images with 12,433 bounding boxes for surface landmine detection, with in-distribution and out-of-distribution splits for domain-shift evaluation [`paper`](https://arxiv.org/abs/2607.28996)

### Medical Imaging
- [RIGA+](https://zenodo.org/record/6325549) — retinal fundus images (BinRushed, Magrabia, MESSIDOR) for optic disc/cup segmentation
- [SCGM](http://niftyweb.cs.ucl.ac.uk/challenge/index.php) — spinal cord gray matter segmentation, multi-site MRI

### Video / Action Recognition
- [UCF-101](https://www.crcv.ucf.edu/data/UCF101.php) — 101 action classes, 13,320 clips
- [HMDB-51](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/) — 51 action classes, 6,766 clips

### Document Analysis
- [SFDLA / DLAdapter](https://github.com/s3setewe/sfdla-DLAdapter) — first benchmark for source-free document layout analysis [`paper`](https://arxiv.org/abs/2503.18742)

## Contribution
If you have published a high-quality paper or come across one that you think is valuable, feel free to contribute! To submit a paper, please open an issue and include the following information in the specified format:
```
- Title of the Paper [`paper`](https://example.com/paper) [`code`](https://example.com/code) `Venue'YY`
```
