# Awesome Source‑Free Domain Adaptation (SFDA) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated resources for Source‑Free Domain Adaptation (SFDA): methods that adapt using only a trained source model (no source data). Includes papers, code, datasets, benchmarks, and tutorials.
<!--lint disable awesome-github repo-url -->

## Contents
- [Surveys & Theory](#surveys--theory)
- [Applications](#applications)
  - [Image Classification](#image-classification)
  - [Object Detection](#object-detection)
  - [Semantic Segmentation (2D)](#semantic-segmentation-2d)
  - [3D / Point Cloud](#3d--point-cloud)
  - [Medical Imaging](#medical-imaging)
  - [Video / Action Recognition](#video--action-recognition)
  - [Face Anti-Spoofing](#face-anti-spoofing)
  - [Human Pose Estimation](#human-pose-estimation)
  - [Image Super-Resolution](#image-super-resolution)
- [Settings & Extensions](#settings--extensions)
  - [Test-Time Adaptation (TTA)](#test-time-adaptation-tta)
  - [Open-Set / Class Distribution Shift](#open-set--class-distribution-shift)
  - [Continual / Class-Incremental SFDA](#continual--class-incremental-sfda)
  - [Multi-Source SFDA](#multi-source-sfda)
  - [Cross-Modal SFDA](#cross-modal-sfda)
  - [Foundation Models / VLM-based](#foundation-models--vlm-based)
  - [Noisy Labels in SFDA](#noisy-labels-in-sfda)
  - [Security / Privacy](#security--privacy)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contribution](#contribution)

Within each section, entries are sorted by year (descending) and then alphabetically by title.

## Surveys & Theory
- A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) [[paper](https://ieeexplore.ieee.org/document/10452835)] [[arxiv](https://arxiv.org/abs/2302.11803)]
- Understanding and Improving Source-free Domain Adaptation from a Theoretical Perspective (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/html/Mitsuzumi_Understanding_and_Improving_Source-free_Domain_Adaptation_from_a_Theoretical_Perspective_CVPR_2024_paper.html)] [[code](https://github.com/nttcslab/improved_sfda)]
- Unraveling the Mysteries of Label Noise in Source-Free Domain Adaptation: Theory and Practice (TPAMI 2025) [[paper](https://www.computer.org/csdl/journal/tp/2025/05/10858421/23VPxGAlL4Q)] [[code](https://github.com/xugezheng/labelNoiseInSFDA)]

## Applications

### Image Classification
- Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation (NeurIPS 2025) [[arxiv](https://arxiv.org/abs/2510.25279)]
- Effective dual-region augmentation for reduced reliance on large amounts of labeled data (2025) [[paper](https://doi.org/10.1117/12.3058627)] [[arxiv](https://arxiv.org/abs/2504.13077)] [[code](https://github.com/PrasannaPulakurthi/Foreground-Background-Augmentation)]
- Label Calibration in Source Free Domain Adaptation (WACV 2025) [[paper](https://openaccess.thecvf.com/content/WACV2025/html/Rai_Label_Calibration_in_Source_Free_Domain_Adaptation_WACV_2025_paper.html)] [[arxiv](https://arxiv.org/abs/2501.07072)]
- Proxy Denoising for Source-Free Domain Adaptation (ICLR 2025) [[paper](https://openreview.net/forum?id=FIj9IEPCKr)] [[arxiv](https://arxiv.org/abs/2406.01658)]
- Revisiting Source-Free Domain Adaptation: a New Perspective via Uncertainty Control (ICLR 2025) [[paper](https://openreview.net/pdf?id=nx9Z5Kva96)] [[code](https://github.com/xugezheng/UCon_SFDA)]
- Revisiting Source-Free Domain Adaptation: Insights into Representativeness, Generalization, and Variety (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Revisiting_Source-Free_Domain_Adaptation_Insights_into_Representativeness_Generalization_and_Variety_CVPR_2025_paper.html)]
- Shuffle PatchMix Augmentation with Confidence-Margin Weighted Pseudo-Labels for Enhanced Source-Free Domain Adaptation (ICIP 2025) [[paper](https://ieeexplore.ieee.org/document/11084606)] [[arxiv](https://arxiv.org/abs/2505.24216)] [[code](https://github.com/PrasannaPulakurthi/SPM)]
- Aligning Non-Causal Factors for Transformer-Based Source-Free Domain Adaptation (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/html/Sanyal_Aligning_Non-Causal_Factors_for_Transformer-Based_Source-Free_Domain_Adaptation_WACV_2024_paper.html)]
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) [[paper](https://ieeexplore.ieee.org/document/10561561)]
- Hierarchical Unsupervised Relation Distillation for Source-Free Domain Adaptation (ECCV 2024) [[paper](https://eccv.ecva.net/virtual/2024/poster/1198)]
- Neighborhood-Aware Mutual Information Maximization for SFDA (TMM 2024) [[paper](https://ieeexplore.ieee.org/document/10510655)]
- SF(DA)²: Source-free Domain Adaptation Through the Lens of Data Augmentation (ICLR 2024) [[paper](https://openreview.net/pdf?id=kUCgHbmO11)] [[arxiv](https://arxiv.org/abs/2312.08566)] [[code](https://github.com/shinyflight/SFDA2)]
- SFDA with Diffusion-Guided Source Data Generation (arXiv 2024) [[paper](https://arxiv.org/abs/2402.04929)]
- Visually Source-Free Domain Adaptation via Adversarial Style Matching (TIP 2024) [[paper](https://ieeexplore.ieee.org/document/10410236)]
- Class Relationship Embedded Learning for Source-Free Unsupervised Domain Adaptation (CVPR 2023) [[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_Class_Relationship_Embedded_Learning_for_Source-Free_Unsupervised_Domain_Adaptation_CVPR_2023_paper.html)] [[code](https://github.com/zhyx12/CRCo)]
- Domain-Specificity Inducing Transformers for Source-Free Domain Adaptation (DSiT) (ICCV 2023) [[arxiv](https://arxiv.org/abs/2308.14023)]
- Guiding Pseudo-Labels with Uncertainty Estimation for Source-Free Unsupervised Domain Adaptation (PLUE) (CVPR 2023) [[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Litrico_Guiding_Pseudo-Labels_With_Uncertainty_Estimation_for_Source-Free_Unsupervised_Domain_Adaptation_CVPR_2023_paper.html)]
- Rethinking the Role of Pre-Trained Networks in Source-Free Domain Adaptation (ICCV 2023) [[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Rethinking_the_Role_of_Pre-Trained_Networks_in_Source-Free_Domain_Adaptation_ICCV_2023_paper.html)]
- Source-Free Domain Adaptation via Target Prediction Distribution Searching (TPDS) (IJCV 2023) [[paper](https://link.springer.com/article/10.1007/s11263-023-01892-w)]
- Adaptive Contrastive Learning with Label Consistency for Source Data Free Unsupervised Domain Adaptation (Sensors 2022) [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9185254/)]
- Attracting and Dispersing: A Simple Approach for Source-free Domain Adaptation (AaD) (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2205.04183)] [[code](https://github.com/Albert0147/AaD_SFDA)]
- Balancing Discriminability and Transferability for Source-Free Domain Adaptation (ICML 2022) [[paper](https://proceedings.mlr.press/v162/kundu22a.html)]
- Confidence Score for Source-Free Unsupervised Domain Adaptation (CoWA) (ICML 2022) [[paper](https://proceedings.mlr.press/v162/lee22c.html)]
- Divide and Contrast: Source-free Domain Adaptation via Adaptive Contrastive Learning (DaC) (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2211.06612)] [[code](https://github.com/ZyeZhang/DaC)]
- Exploring Domain-Invariant Parameters for Source Free Domain Adaptation (CVPR 2022) [[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Exploring_Domain-Invariant_Parameters_for_Source_Free_Domain_Adaptation_CVPR_2022_paper.html)]
- Model Adaptation: Historical Contrastive Learning for Unsupervised Domain Adaptation without Source Data (HCL) (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2110.03374)]
- Semantic Consistency Learning on Manifold for Source Data-Free Unsupervised Domain Adaptation (SCLM) (Neural Networks 2022) [[paper](https://www.sciencedirect.com/science/article/pii/S0893608022001897)]
- Source-Free Domain Adaptation via Distribution Estimation (SFDA-DE) (CVPR 2022) [[arxiv](https://arxiv.org/abs/2204.11257)]
- Variational Model Perturbation for Source-Free Domain Adaptation (VMP) (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2210.10378)]
- Adaptive Adversarial Network for Source-Free Domain Adaptation (A2Net) (ICCV 2021) [[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Xia_Adaptive_Adversarial_Network_for_Source-Free_Domain_Adaptation_ICCV_2021_paper.html)]
- Casting a BAIT for Offline and Online Source-free Domain Adaptation (CVIU 2021) [[arxiv](https://arxiv.org/abs/2010.12427)]
- Domain Impression: A Source Data Free Domain Adaptation Method (WACV 2021) [[paper](https://openaccess.thecvf.com/content/WACV2021/html/Kurmi_Domain_Impression_A_Source_Data_Free_Domain_Adaptation_Method_WACV_2021_paper.html)]
- Exploiting the Intrinsic Neighborhood Structure for Source-free Domain Adaptation (NRC) (NeurIPS 2021) [[arxiv](https://arxiv.org/abs/2110.04202)] [[code](https://github.com/Albert0147/NRC_SFDA)]
- Generalized Source-Free Domain Adaptation (G-SFDA) (ICCV 2021) [[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_Generalized_Source-Free_Domain_Adaptation_ICCV_2021_paper.html)] [[arxiv](https://arxiv.org/abs/2108.01614)]
- Model Adaptation through Hypothesis Transfer with Gradual Knowledge Distillation (GKD) (IROS 2021) [[paper](https://ieeexplore.ieee.org/abstract/document/9636206)]
- Source Data-absent Unsupervised Domain Adaptation through Hypothesis Transfer and Labeling Transfer (SHOT++) (TPAMI 2021) [[paper](https://ieeexplore.ieee.org/abstract/document/9512429)] [[arxiv](https://arxiv.org/abs/2012.07297)] [[code](https://github.com/tim-learn/SHOT-plus)]
- Source-free Domain Adaptation via Avatar Prototype Generation and Adaptation (CPGA) (IJCAI 2021) [[arxiv](https://arxiv.org/abs/2106.15326)]
- Do We Really Need to Access the Source Data? Source Hypothesis Transfer for Unsupervised Domain Adaptation (SHOT) (ICML 2020) [[paper](http://proceedings.mlr.press/v119/liang20a/liang20a.pdf)] [[arxiv](https://arxiv.org/abs/2002.08546)] [[code](https://github.com/tim-learn/SHOT)]
- Model Adaptation: Unsupervised Domain Adaptation Without Source Data (CVPR 2020) [[paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Model_Adaptation_Unsupervised_Domain_Adaptation_Without_Source_Data_CVPR_2020_paper.html)]

### Object Detection
- Simplifying Source-Free Domain Adaptation for Object Detection (ECCV 2024) [[paper](https://link.springer.com/chapter/10.1007/978-3-031-72949-2_12)] [[arxiv](https://arxiv.org/abs/2407.07586)] [[code](https://github.com/EPFL-IMOS/simple-SFOD)]
- Source-Free Domain Adaptation for YOLO Object Detection (ECCV 2024) [[paper](https://dl.acm.org/doi/10.1007/978-3-031-91672-4_14)] [[arxiv](https://arxiv.org/pdf/2409.16538)] [[code](https://github.com/vs-cv/sf-yolo)]
- Instance Relation Graph Guided Source-Free Domain Adaptive Object Detection (CVPR 2022) [[arxiv](https://arxiv.org/abs/2203.15793)] [[code](https://github.com/Vibashan/irg-sfda)]
- Source-Free Object Detection by Learning To Overlook Domain Style (LODS) (CVPR 2022) [[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Source-Free_Object_Detection_by_Learning_To_Overlook_Domain_Style_CVPR_2022_paper.html)]

### Semantic Segmentation (2D)
- SFDA for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) [[paper](https://arxiv.org/abs/2305.14269)]
- Stable Neighbor Denoising for Source-free Domain Adaptive Segmentation (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_Stable_Neighbor_Denoising_for_Source-free_Domain_Adaptive_Segmentation_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2406.06813)] [[code](https://github.com/DZhaoXd/SND)]
- Generalize Then Adapt: Source-Free Domain Adaptive Semantic Segmentation (ICCV 2021) [[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Kundu_Generalize_Then_Adapt_Source-Free_Domain_Adaptive_Semantic_Segmentation_ICCV_2021_paper.html)]
- Source-Free Domain Adaptation for Semantic Segmentation (CVPR 2021) [[paper](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_Source-Free_Domain_Adaptation_for_Semantic_Segmentation_CVPR_2021_paper.html)]

### 3D / Point Cloud
- PointSFDA: Source-free Domain Adaptation for Point Cloud Completion (arXiv 2025) [[arxiv](https://arxiv.org/abs/2503.15144)] [[code](https://github.com/Starak-x/PointSFDA)]
- Towards Stable and Robust Source-free Unsupervised 3D Semantic Segmentation (ECCV 2024) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02968.pdf)]

### Medical Imaging
- AIF-SFDA: Autonomous Information Filter-driven Source-Free Domain Adaptation for Medical Image Segmentation (AAAI 2025) [[arxiv](https://arxiv.org/abs/2501.03074)] [[code](https://github.com/JingHuaMan/AIF-SFDA)]
- ProSFDA: Source-free Domain Adaptation Using Prompt Learning for Medical Image Segmentation (Pattern Recognition 2025) [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325009513)] [[code](https://github.com/ShishuaiHu/ProSFDA)]
- VP-SFDA: Visual Prompt Source-Free Domain Adaptation for Cross-Modal Medical Image Segmentation (Health Data Science 2025) [[paper](https://spj.science.org/doi/10.34133/hds.0143)]
- Robust Source-Free Domain Adaptation for Fundus Image Segmentation (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/papers/Li_Robust_Source-Free_Domain_Adaptation_for_Fundus_Image_Segmentation_WACV_2024_paper.pdf)] [[code](https://github.com/LinGrayy/PLPB)]

### Video / Action Recognition
- Source-free Video Domain Adaptation by Learning from Noisy Labels (Pattern Recognition 2025) [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320324010793)] [[code](https://github.com/avijit9/CleanAdapt)]
- Source-Free Video Domain Adaptation With Spatial-Temporal-Historical Consistency Learning (CVPR 2023) [[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Source-Free_Video_Domain_Adaptation_With_Spatial-Temporal-Historical_Consistency_Learning_CVPR_2023_paper.html)]
- Source-free Video Domain Adaptation by Learning Temporal Consistency for Action Recognition (ATCoN) (ECCV 2022) [[arxiv](https://arxiv.org/abs/2203.04559)] [[code](https://github.com/xuyu0010/ATCoN)]

### Face Anti-Spoofing
- Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimal_Transport-Guided_Source-Free_Adaptation_for_Face_Anti-Spoofing_CVPR_2025_paper.html)] [[arxiv](https://arxiv.org/abs/2503.22984)]

### Human Pose Estimation
- Prior-guided Source-free Domain Adaptation for Human Pose Estimation (ICCV 2023) [[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Raychaudhuri_Prior-guided_Source-free_Domain_Adaptation_for_Human_Pose_Estimation_ICCV_2023_paper.html)]

### Image Super-Resolution
- Uncertainty-Aware Source-Free Adaptive Image Super-Resolution with Wavelet Augmentation Transformer (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Ai_Uncertainty-Aware_Source-Free_Adaptive_Image_Super-Resolution_with_Wavelet_Augmentation_Transformer_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2303.17783)] [[code](https://github.com/shallowdream204/SODA-SR)]

## Settings & Extensions

### Test-Time Adaptation (TTA)
- EcoTTA: Memory-Efficient Continual Test-Time Adaptation via Self-Distilled Regularization (CVPR 2023) [[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Song_EcoTTA_Memory-Efficient_Continual_Test-Time_Adaptation_via_Self-Distilled_Regularization_CVPR_2023_paper.html)]
- Towards Stable Test-Time Adaptation in Dynamic Wild World (SAR) (ICLR 2023) [[arxiv](https://arxiv.org/abs/2302.12400)]
- DELTA: Degradation-Free Fully Test-Time Adaptation (ICLR 2023) [[arxiv](https://arxiv.org/abs/2301.13018)]
- Contrastive Test-Time Adaptation (AdaContrast) (CVPR 2022) [[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_Contrastive_Test-Time_Adaptation_CVPR_2022_paper.html)] [[code](https://github.com/DianCh/AdaContrast)]
- Continual Test-Time Domain Adaptation (CoTTA) (CVPR 2022) [[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Wang_Continual_Test-Time_Domain_Adaptation_CVPR_2022_paper.html)] [[code](https://github.com/qinenergy/cotta)]
- Efficient Test-Time Model Adaptation without Forgetting (EATA) (ICML 2022) [[paper](https://proceedings.mlr.press/v162/niu22a.html)] [[code](https://github.com/mr-eggplant/EATA)]
- MEMO: Test Time Robustness via Adaptation and Augmentation (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2110.09506)]
- NOTE: Robust Continual Test-time Adaptation Against Temporal Correlation (NeurIPS 2022) [[arxiv](https://arxiv.org/abs/2208.05117)]
- Tent: Fully Test-Time Adaptation by Entropy Minimization (ICLR 2021) [[arxiv](https://arxiv.org/abs/2006.10726)]

### Open-Set / Class Distribution Shift
- Distinguish Then Exploit: Source-free Open Set Domain Adaptation via Weight Barcode Estimation and Sparse Label Assignment (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.html)] [[pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Distinguish_Then_Exploit_Source-free_Open_Set_Domain_Adaptation_via_Weight_CVPR_2025_paper.pdf)]
- Robust Nearest Neighbors for Source-Free Domain Adaptation under Class Distribution Shift (ECCV 2024) [[paper](https://eccv.ecva.net/virtual/2024/poster/833)] [[code](https://github.com/CyberAgentAILab/Robust_Nearest_Neighbors_SFDA-CDS)]
- Unveiling the Unknown: Unleashing the Power of Unknown to Known in Open-Set Source-Free Domain Adaptation (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Wan_Unveiling_the_Unknown_Unleashing_the_Power_of_Unknown_to_Known_CVPR_2024_paper.pdf)] [[code](https://github.com/xdwfl/UPUK)]
- Universal Source-Free Domain Adaptation (CVPR 2020) [[paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Kundu_Universal_Source-Free_Domain_Adaptation_CVPR_2020_paper.html)]

### Continual / Class-Incremental SFDA
- Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation (CVPR 2025) [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Multi-Granularity_Class_Prototype_Topology_Distillation_for_Class-Incremental_Source-Free_Unsupervised_Domain_CVPR_2025_paper.html)]
- CoSDA: Continual Source-Free Domain Adaptation (ICLR 2023) [[arxiv](https://arxiv.org/abs/2304.06627)]

### Multi-Source SFDA
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) [[paper](https://arxiv.org/abs/2402.08249)]
- Unsupervised Multi-Source Domain Adaptation Without Access to Source Data (CVPR 2021) [[paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ahmed_Unsupervised_Multi-Source_Domain_Adaptation_Without_Access_to_Source_Data_CVPR_2021_paper.html)]

### Cross-Modal SFDA
- EventDance: Unsupervised Source-free Cross-modal Adaptation for Event-based Object Recognition (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zheng_EventDance_Unsupervised_Source-free_Cross-modal_Adaptation_for_Event-based_Object_Recognition_CVPR_2024_paper.pdf)] [[code](https://github.com/zhengxujosh/EventDance)]

### Foundation Models / VLM-based
- Source-Free Domain Adaptation with Frozen Multimodal Foundation Model (CVPR 2024) [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Tang_Source-Free_Domain_Adaptation_with_Frozen_Multimodal_Foundation_Model_CVPR_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2311.16510)] [[code](https://github.com/tntek/source-free-domain-adaptation)]
- ReCLIP: Refine Contrastive Language Image Pre-Training with SFDA (WACV 2024) [[paper](https://openaccess.thecvf.com/content/WACV2024/papers/Hu_ReCLIP_Refine_Contrastive_Language_Image_Pre-Training_With_Source_Free_Domain_WACV_2024_paper.pdf)] [[arxiv](https://arxiv.org/abs/2308.03793)] [[code](https://github.com/michiganleon/ReCLIP_WACV)]

### Noisy Labels in SFDA
- ElimPCL: Eliminating Noise Accumulation with Progressive Curriculum Labeling for Source-Free Domain Adaptation (arXiv 2025) [[arxiv](https://arxiv.org/abs/2503.23712)]
- De-Confusing Pseudo-Labels in Source-Free Domain Adaptation (ECCV 2024) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10138.pdf)] [[arxiv](https://arxiv.org/abs/2401.01650)] [[code](https://github.com/ssi-research/DCPL_SFDA)]
- When Source-Free Domain Adaptation Meets Learning with Noisy Labels (ICLR 2023) [[arxiv](https://arxiv.org/abs/2301.13381)] [[code](https://github.com/liyi01827/SFDA_LLN)]

### Security / Privacy
- SSDA: Secure Source-Free Domain Adaptation (ICCV 2023) [[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Ahmed_SSDA_Secure_Source-Free_Domain_Adaptation_ICCV_2023_paper.html)] [[code](https://github.com/ML-Security-Research-LAB/SSDA)]

## Datasets & Benchmarks

### Image Classification
- [Office-31](https://drive.google.com/file/d/0B4IapRTv9pJ1WGZVd1VDMmhwdlE/view?resourcekey=0-gNMHVtZfRAyO_t2_WrOunA) — 31 classes, 3 domains (Amazon, DSLR, Webcam)
- [Office-Home](https://www.hemanthdv.org/officeHomeDataset.html) — 65 classes, 4 domains (Art, Clipart, Product, Real World)
- [VisDA-C](https://github.com/VisionLearningGroup/taskcv-2017-public/tree/master/classification) — 12 classes, synthetic-to-real
- [DomainNet (cleaned)](http://ai.bu.edu/M3SDA/) — 345 classes, 6 domains (Clipart, Infograph, Painting, Quickdraw, Real, Sketch)
- [PACS](https://domaingeneralization.github.io/) — 7 classes, 4 domains (Photo, Art, Cartoon, Sketch)
- [Digits](http://yann.lecun.com/exdb/mnist/) — MNIST / USPS / SVHN cross-domain digit recognition

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

### Medical Imaging
- [RIGA+](https://zenodo.org/record/6325549) — retinal fundus images (BinRushed, Magrabia, MESSIDOR) for optic disc/cup segmentation
- [SCGM](http://niftyweb.cs.ucl.ac.uk/challenge/index.php) — spinal cord gray matter segmentation, multi-site MRI

### Video / Action Recognition
- [UCF-101](https://www.crcv.ucf.edu/data/UCF101.php) — 101 action classes, 13,320 clips
- [HMDB-51](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/) — 51 action classes, 6,766 clips

## Contribution
If you have published a high-quality paper or come across one that you think is valuable, feel free to contribute! To submit a paper, please open an issue and include the following information in the specified format:
```
- Title (Venue/Year) [[paper](https://example.com/paper)] [[code](https://example.com/code)] [[project](https://example.com/site)]
```
