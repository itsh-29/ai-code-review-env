---
title: AI Code Review Environment
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# 🚀 AI Code Review Environment (OpenEnv Compatible)

## 🧠 Overview

This project implements a **real-world AI evaluation environment** for code review tasks using the OpenEnv framework.

The environment simulates how an AI agent analyzes code and performs:

* Syntax error detection
* Logic bug identification
* Optimization suggestions

Unlike simple classification tasks, this environment also evaluates the **quality of explanations**, making it closer to real-world LLM evaluation systems.

---

## 🎯 Objectives

* Build a realistic environment for training and evaluating AI agents
* Provide multi-level difficulty tasks (easy → medium → hard)
* Implement a **reward function with partial scoring and reasoning-based bonuses**
* Ensure compatibility with **OpenEnv API (step/reset/state)**

---

## 🧩 Environment Design

### 🔹 Observation Space

Each observation contains:

```json
{
  "code": "def add(a,b): return a-b",
  "difficulty": "medium"
}
```

---

### 🔹 Action Space

The agent must return:

```json
{
  "label": "logic_error",
  "explanation": "incorrect operator used"
}
```

#### Possible Labels:

* `syntax_error`
* `logic_error`
* `optimization_suggestion`
* `no_issue`

---

## 🏆 Tasks

The environment includes **3 levels of difficulty**:

| Difficulty | Description                                             |
| ---------- | ------------------------------------------------------- |
| 🟢 Easy    | Syntax errors (missing colon, indentation issues)       |
| 🟡 Medium  | Logical bugs (wrong operator, incorrect condition)      |
| 🔴 Hard    | Optimization improvements (inefficient loops, patterns) |

---

## 💰 Reward Function

The reward is designed to reflect real-world evaluation:

### Base Reward:

* ✅ Correct label → **+0.7**
* ❌ Incorrect label → **+0.2**

### Explanation Bonus:

* Adds **+0.3** if explanation matches expected reasoning

Examples:

* Syntax error → explanation contains `"missing"`
* Logic error → explanation contains `"wrong"`
* Optimization → explanation contains `"faster"`

### Final Reward Range:

```
0.0 → 1.0
```

---

## ⚙️ OpenEnv API Implementation

The environment follows the standard OpenEnv interface:

* `reset()` → returns initial observation
* `step(action)` → returns `(observation, reward, done, info)`
* `state()` → returns current environment state

---

## ▶️ How to Run (Local)

### 1. Clone / Download project

```bash
git clone <your-repo-url>
cd code-review-env
```

### 2. Run the baseline agent

```bash
python inference.py
```

---

## 🧪 Example Output

```
Code: def add(a,b): return a-b
Difficulty: medium
Prediction: {'label': 'logic_error', 'explanation': 'wrong operation used'}
Reward: 1.0

FINAL SCORES:
easy : 0.46
medium : 0.2
hard : 1.0
```

---

## 🤖 Baseline Agent

A simple rule-based agent is provided in `inference.py`.

It simulates imperfect AI behavior using:

* Pattern matching
* Randomized predictions

This ensures **realistic, non-perfect performance**.

---

## 🐳 Docker Support

Build and run using Docker:

```bash
docker build -t code-review-env .
docker run code-review-env
```

---

## 🚀 Deployment (HuggingFace Spaces)

This project is fully compatible with OpenEnv deployment:

```bash
openenv push --repo-id your-username/code-review-env
```

---

## 📁 Project Structure

```
code-review-env/
│
├── environment.py     # Core environment logic
├── env.py             # OpenEnv wrapper
├── inference.py       # Baseline agent
├── openenv.yaml       # Environment config
├── Dockerfile         # Container setup
├── requirements.txt
└── README.md
```

---

## 💡 Key Features

* ✅ Real-world task simulation (code review)
* ✅ Multi-difficulty task design
* ✅ Explanation-based reward shaping
* ✅ OpenEnv compliant API
* ✅ Reproducible baseline evaluation

---

## 🧠 Why This Matters

Modern AI systems are not evaluated only on correctness, but also on **reasoning and explainability**.

This environment:

* Encourages interpretable AI behavior
* Simulates real engineering workflows
* Provides a scalable evaluation framework

---

## 👨‍💻 Author

Developed as part of a hackathon project focused on building real-world AI environments.

---

## 📌 Future Improvements

* Add real-world GitHub code datasets
* Integrate LLM-based agents
* Multi-step reasoning tasks
* Web UI for visualization

---
