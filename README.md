# Awesome Source‑Free Domain Adaptation (SFDA) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Description
Curated resources for Source‑Free Domain Adaptation (SFDA): methods that adapt using only a trained source model (no source data). Includes papers, code, datasets, benchmarks, and tutorials.
<!--lint disable awesome-github -->

## Contents
- [Recent (2024+)](#recent-2024)
- [Surveys](#surveys)
- [Methods — Closed-set](#methods--closed-set)
- [Methods — Open-set / Partial / Universal](#methods--open-set--partial--universal)
- [Tasks — Image Classification](#tasks--image-classification)
- [Tasks — Semantic Segmentation](#tasks--semantic-segmentation)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Libraries & Tooling](#libraries--tooling)
- [Tutorials & Talks](#tutorials--talks)
- [Related](#related)
- [Contributing](#contributing)

## Recent (2024+)
- Understanding and Improving Source-Free Domain Adaptation from a Theoretical Perspective (CVPR 2024) — theory-grounded analysis with practical improvements for SFDA. [details](#cvpr2024-theory-sfda)
- Source-Free Domain Adaptation with Frozen Multimodal Foundation Model (CVPR 2024) — adapts target data by leveraging frozen multimodal foundation model features. [details](#cvpr2024-frozen-mm)
- GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) — graph diffusion and jigsaw-based alignment for robust SFDA. [details](#tpami2024-gala)
- A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) — broad survey of settings, methods, tasks, and benchmarks for SFDA. [details](#tpami2024-survey-sfda)
- Visually Source-Free Domain Adaptation via Adversarial Style Matching (TIP 2024) — adversarial style matching without access to source data. [details](#tip2024-visually-sfda)
- ReCLIP: Refine Contrastive Language Image Pre-Training with Source Free Domain Adaptation (WACV 2024) — aligns CLIP features to the target domain under SFDA. [details](#wacv2024-reclip)
- Neighborhood-Aware Mutual Information Maximization for Source-Free Domain Adaptation (TMM 2024) — mutual information based objective for SFDA. [details](#tmm2024-nmi)
- SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) — multi-source-free adaptation via model separation. [details](#arxiv2024-seprep-net)
- Source-Free Domain Adaptation with Diffusion-Guided Source Data Generation (arXiv 2024) — synthesizes source-like data via diffusion to aid SFDA. [details](#arxiv2024-diffusion-guided)
- SF(DA)^2: Source-free Domain Adaptation Through the Lens of Data Augmentation (arXiv 2024) — analyzes and leverages data augmentation for SFDA. [details](#arxiv2024-sfda2-augmentation)
- Source-Free Domain Adaptation for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) — extends SFDA to RGB-D segmentation with ViTs. [details](#arxiv2024-rgbd-vit)

## Surveys
- <a id="tpami2024-survey-sfda"></a> A Comprehensive Survey on Source-Free Domain Adaptation (TPAMI 2024) — broad survey of SFDA problem settings, methods, and benchmarks. [paper](https://doi.org/10.1109/tpami.2024.3370978)

## Methods — Closed-set
- <a id="tpami2024-gala"></a> GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation (TPAMI 2024) — graph diffusion and jigsaw-based alignment for robust SFDA. [paper](https://doi.org/10.1109/tpami.2024.3416372)
- <a id="tmm2024-nmi"></a> Neighborhood-Aware Mutual Information Maximization for Source-Free Domain Adaptation (TMM 2024) — mutual information based objective for SFDA. [paper](https://doi.org/10.1109/tmm.2024.3394971)
- <a id="wacv2024-reclip"></a> ReCLIP: Refine Contrastive Language Image Pre-Training with Source Free Domain Adaptation (WACV 2024) — aligns CLIP features to the target domain under SFDA. [paper](https://doi.org/10.1109/wacv57701.2024.00297)
- <a id="arxiv2024-sfda2-augmentation"></a> SF(DA)^2: Source-free Domain Adaptation Through the Lens of Data Augmentation (arXiv 2024) — analyzes and leverages data augmentation for SFDA. [paper](https://arxiv.org/abs/2403.10834)
- <a id="arxiv2024-seprep-net"></a> SepRep-Net: Multi-source Free Domain Adaptation via Model Separation and Reparameterization (arXiv 2024) — multi-source-free adaptation via model separation. [paper](https://arxiv.org/abs/2402.08249)
- <a id="arxiv2024-diffusion-guided"></a> Source-Free Domain Adaptation with Diffusion-Guided Source Data Generation (arXiv 2024) — synthesizes source-like data via diffusion to aid SFDA. [paper](https://arxiv.org/abs/2402.04929)
- <a id="cvpr2024-frozen-mm"></a> Source-Free Domain Adaptation with Frozen Multimodal Foundation Model (CVPR 2024) — adapts target data by leveraging frozen multimodal foundation model features. [paper](https://doi.org/10.1109/cvpr52733.2024.02238)
- <a id="cvpr2024-theory-sfda"></a> Understanding and Improving Source-Free Domain Adaptation from a Theoretical Perspective (CVPR 2024) — theory-grounded analysis with practical improvements for SFDA. [paper](https://doi.org/10.1109/cvpr52733.2024.02694)
- <a id="tip2024-visually-sfda"></a> Visually Source-Free Domain Adaptation via Adversarial Style Matching (TIP 2024) — adversarial style matching without access to source data. [paper](https://doi.org/10.1109/tip.2024.3353539)

## Methods — Open-set / Partial / Universal
- Add open/partial/universal SFDA methods here.

## Tasks — Image Classification
- Add image classification SFDA resources here.

## Tasks — Semantic Segmentation
- <a id="arxiv2024-rgbd-vit"></a> Source-Free Domain Adaptation for RGB-D Semantic Segmentation with Vision Transformers (arXiv 2024) — extends SFDA to RGB-D segmentation with ViTs. [paper](https://arxiv.org/pdf/2305.14269)

## Datasets & Benchmarks
- DomainNet — multi‑domain classification benchmark.
- Office‑31 / Office‑Home — classic DA suites, widely reused in SFDA.
- VisDA‑2017 — synthetic→real; used by SFDA methods.

## Libraries & Tooling
- Add libraries and tooling here.

## Tutorials & Talks
- Add tutorials and talks here.

## Related
- Awesome Domain Adaptation — broader DA resources.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md). Use this entry format:

```
- [Title (Venue/Year)](https://example.com/paper) — one sentence summary. [code](https://example.com/code) [project](https://example.com/site)
```

Sorting policy:
- Sort entries alphabetically by title within each section.
- Additionally, mirror 2024+ entries into the Recent (2024+) block (sorted newest first).
