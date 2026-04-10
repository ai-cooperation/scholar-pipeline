---
title: "A Generalizable Load Recognition Method in NILM Based on Transferable Random Forest"
source: semantic-scholar
keyword: "NILM"
year: 2025
authors: ["Zhongzong Yan", "Pengfei Hao", "M. Nardello", "Davide Brunelli", "He Wen"]
doi: "10.1109/TIM.2025.3570355"
arxiv: ""
citations: 33
is_open_access: false
tags: [nilm]
content_layer: L1
fetched: "2026-04-10"
---

## Abstract

Practical applications of nonintrusive load monitoring (NILM) require load recognition models that generalize to unseen data from new houses and operate efficiently on edge devices. However, existing NILM approaches, particularly deep learning (DL) models, are computationally intensive and prone to performance degradation when deployed to new houses due to domain shifts. To address these challenges, this article proposes a weighted transferable random forest (WTRF) approach for load recognition. Based on the random forest (RF) framework, WTRF incorporates a transfer learning (TL) mechanism to swiftly adapt the model to new houses using only one to three labeled samples per appliance. The model is lightweight, with a memory size under 300 kB. Case studies on three datasets demonstrate its effectiveness, including a macro <inline-formula> <tex-math notation="LaTeX">$F1$ </tex-math></inline-formula>-score of 97.0% <inline-formula> <tex-math notation="LaTeX">$\pm ~2.6$ </tex-math></inline-formula>% when transferring from PLAID to WHITED, a significant improvement over 5.7% <inline-formula> <tex-math notation="LaTeX">$\pm ~1.7$ </tex-math></inline-formula>% achieved by source-only models. Deployed on a Raspberry Pi 4, WTRF achieves update times as low as <inline-formula> <tex-math notation="LaTeX">$3.1 \pm 0.3$ </tex-math></inline-formula>s and testing times of approximately 3 ms per house. These results highlight WTRF’s efficiency in addressing domain shifts and its suitability for real-time NILM in resource-constrained edge environments.

## Metadata

- **DOI**: https://doi.org/10.1109/TIM.2025.3570355
- **ArXiv**: N/A
- **Semantic Scholar**: https://www.semanticscholar.org/paper/628dfc8418355cd3db8f5dc2abd15f8a2e8b65c1
- **Open Access PDF**: N/A
- **Citations**: 33
- **Authors**: Zhongzong Yan, Pengfei Hao, M. Nardello, Davide Brunelli, He Wen
