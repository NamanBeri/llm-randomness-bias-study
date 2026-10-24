# 🎲 LLM Pseudorandomness & Cognitive Bias Empirical Study

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

An empirical evaluation investigating why Large Language Models (LLMs) fail at generating pseudo-random numbers and how human cognitive biases leak into autoregressive transformer weights.

---

## 📌 Key Findings at a Glance

* **The "Lucky 7" Mode Collapse**: Across **900+ trials** at $T = 0.8$, **60.9%** of non-thinking generations collapsed onto **7** (peaking at **94.0%** in Qwen3.5-4B).
* **Anti-Repetition Ping-Pong**: Forcing the model with previous choices (`Prev 1 Choice = 7`) caused an immediate recoil to human secondary cognitive prior: **3**.
* **Prompt Token Leakage in Micro-Models**: In sub-1B parameter models (Qwen2.5-0.5B), the prompt boundary token `"1"` in *"between 1 and 10"* directly spilled over into output prediction (38.8% spike at 1).
* **Dead Zones**: Digits **2 (0.11%)** and **10 (0.22%)** were virtually never generated.

![Selection Distribution](ai_random_number_spike_plot.png)

---

## 📂 Repository Contents

* `*.csv`: Raw empirical dataset runs across 3 model architectures and 4 memory states.
* `analyze_results.py`: Standalone script to reproduce metrics and plots.
* `LLM Pseudorandomness & Cognitive Bias Empirical Analysis.pdf`: Full 6-page empirical research paper.
* `MEDIUM_BLOG_DRAFT.md`: Reader-friendly blog draft written for Medium / Substack.

---

## 🔬 Dataset Schema

Each row in the `.csv` files follows this structure:
```csv
timestamp,count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10
```

### Models & Configurations Evaluated:
1. **Qwen2.5-0.5B (397 MB)**: No Context, 1-Choice Context, 2-Choice Context
2. **Qwen3.5-4B (3.3 GB)**: No Context, 1-Choice Context, 2-Choice Context, With CoT Thinking
3. **Gemma4:e4b (6.6 GB)**: No Context, 1-Choice Context, 2-Choice Context

---

## 🚀 Quickstart & Reproduction

### 1. Clone the repository
```bash
git clone https://github.com/NamanBeri/llm-randomness-bias-study.git
cd llm-randomness-bias-study
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib
```

### 3. Run analysis
```bash
python analyze_results.py
```

---

## ⚖️ Takeaway for Developers

> **Never use an LLM as a random number generator.**  
> LLMs are autoregressive token predictors tuned on human cultural data. Use cryptographic or standard pseudorandom number generators (`random.randint()` or `crypto.getRandomValues()`) for games, raffles, and sampling.

---

## 📄 License
This project is licensed under the MIT License - feel free to cite and build upon this research.
