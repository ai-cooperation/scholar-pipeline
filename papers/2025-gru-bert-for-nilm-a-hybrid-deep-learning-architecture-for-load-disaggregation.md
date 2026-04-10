---
title: "GRU-BERT for NILM: A Hybrid Deep Learning Architecture for Load Disaggregation"
source: semantic-scholar
keyword: "NILM"
year: 2025
authors: ["Annysha Huzzat", "A. Khwaja", "Ali A. Alnoman", "Bhagawat Adhikari", "A. Anpalagan"]
doi: "10.3390/ai6090238"
arxiv: ""
citations: 5
is_open_access: false
tags: [nilm]
content_layer: L1
fetched: "2026-04-10"
---

## Abstract

Non-Intrusive Load Monitoring (NILM) aims to disaggregate a household’s total aggregated power consumption into appliance-level usage, enabling intelligent energy management without the need for intrusive metering. While deep learning has improved NILM significantly, existing NILM models struggle to capture load patterns across both longer time intervals and subtle timings for appliances involving brief or overlapping usage patterns. In this paper, we propose a novel GRU+BERT hybrid architecture, exploring both unidirectional (GRU+BERT) and bidirectional (Bi-GRU+BERT) variants. Our model combines Gated Recurrent Units (GRUs) to capture sequential temporal dependencies with Bidirectional Encoder Representations from Transformers (BERT), which is a transformer-based model that captures rich contextual information across the sequence. The bidirectional variant (Bi-GRU+BERT) processes input sequences in both forward (past to future) and backward (future to past) directions, enabling the model to learn relationships between power consumption values at different time steps more effectively. The unidirectional variant (GRU+BERT) provides an alternative suited for appliances with structured, sequential multi-phase usage patterns, such as dishwashers. By placing the Bi-GRU or GRU layer before BERT, our models first capture local time-based load patterns and then use BERT’s self-attention to understand the broader contextual relationships. This design addresses key limitations of both standalone recurrent and transformer-based models, offering improved performance on transient and irregular appliance loads. Evaluated on the UK-DALE and REDD datasets, the proposed Bi-GRU+BERT and GRU+BERT models show competitive performance compared to several state-of-the-art NILM models while maintaining a comparable model size and training time, demonstrating their practical applicability for real-time energy disaggregation, including potential edge and cloud deployment scenarios.

## Metadata

- **DOI**: https://doi.org/10.3390/ai6090238
- **ArXiv**: N/A
- **Semantic Scholar**: https://www.semanticscholar.org/paper/f5ec7f5450eb81da3b0bfcc81fd5596e84a9dd4b
- **Open Access PDF**: N/A
- **Citations**: 5
- **Authors**: Annysha Huzzat, A. Khwaja, Ali A. Alnoman, Bhagawat Adhikari, A. Anpalagan, Isaac Woungang
