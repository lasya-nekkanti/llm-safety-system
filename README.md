# Hybrid AI Safety System for LLM Poisoning & Hallucination Detection

## Overview
Large Language Models (LLMs) integrated with external knowledge sources 
(Retrieval-Augmented Generation, RAG) are vulnerable to **prompt 
injection** and **context poisoning** attacks. These attacks often lead to 
**hallucinated or misleading outputs**, even when the base model is 
strong.

This project implements a **hybrid AI safety system** that:
1. Detects **poisoned or malicious context before generation**
2. Verifies **hallucinations after generation**
3. Demonstrates how layered safety checks surface different failure modes in 
LLM pipelines

The focus is on **system-level AI safety**, not just model accuracy.

---

## Problem Statement
LLM applications frequently trust retrieved documents without verifying 
intent or safety. Malicious instructions hidden in retrieved text can 
override system behavior and cause hallucinations. Post-generation 
filtering alone is insufficient.

**Goal:**  
Build a modular safety layer that detects poisoning before inference and 
verifies hallucinations after inference.



---

## Threat Model
### Attacks Covered
- Prompt Injection
- Context / Document Poisoning

### Out of Scope
- Model weight poisoning
- Supply-chain attacks
- Adversarial token perturbations

---

## Methodology

### 1. Poisoning Detection (Pre-generation)
A **multi-layer defense** is used:

- **Prompt Injection Detector**
  - Flags instruction-override language
- **Intent Mismatch Detector**
  - Uses sentence embeddings to detect semantic divergence between query 
and context

Safety signals are reported before generation to highlight potential risks.

---

### 2. Retrieval-Augmented Generation (RAG Simulation)
- Documents are embedded using Sentence-BERT
- Query–document similarity is computed via cosine similarity
- The most relevant document is retrieved
- The retrieval layer is modular and could be replaced with FAISS in a 
production setting.

---

### 3. Hallucination Detection (Post-generation)
- Uses sentence embedding similarity to compare generated answers with trusted 
reference facts.
- Semantically distant outputs are flagged as potential hallucinations.
- Non-entailed responses are flagged as hallucinations

---

## How to Run

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/lasya-nekkanti/llm-safety-system.git
   cd llm-safety-system

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the demo pipeline:
   ```bash
   python app.py

---

## Evaluation

The system is evaluated qualitatively through controlled example scenarios,
demonstrating how different safety detectors activate under different threat 
conditions.

---


## Technologies Used
- Python
- HuggingFace Sentence Transformers
- Transformer-based Embedding Models (MiniLM)
- Semantic Similarity (Cosine Distance)
- Retrieval-Augmented Generation (RAG)
- Modular AI Safety Techniques

---

## Key Takeaways
- Many LLM hallucinations originate from **poisoned context**
- Pre-generation safety layers are more effective than post-generation 
filtering alone
- AI safety is a **system design problem**, not just a modeling problem

---

## Design Philosophy

This system uses multiple safety detectors, each targeting a different failure 
mode in LLM pipelines.
Not all detectors are expected to activate for every input.

For example:
- **Poisoning detection** flags malicious or instruction-overriding retrieved 
context.
- **Intent mismatch detection** identifies semantic divergence between user 
intent and retrieved data.
- **Hallucination verification** checks whether model outputs are grounded in 
trusted reference facts.

Depending on the threat scenario, some detectors may correctly remain inactive 
while others trigger.
This layered design mirrors real-world LLM safety systems, where defenses are 
specialized rather than redundant.

---

## Future Work
- Replace simulated outputs with real LLM inference
- Add stronger fact-checking models (NLI, external knowledge bases)
- Add CLI or API interface for interactive use
- Expand poisoning detection beyond rule-based patterns
---

## Summary

This project demonstrates a practical, system-level approach to AI safety for
Retrieval-Augmented Generation (RAG) based LLM applications.

Rather than treating hallucinations as a purely model-level issue, the system
shows how unsafe or poisoned context can propagate through the pipeline and
lead to incorrect outputs. By introducing layered safety checks before and
after generation—such as poisoning detection, intent–context alignment 
analysis,
and hallucination verification—the project highlights how many LLM failures
can be mitigated through better system design.

The implementation prioritizes modularity, interpretability, and realistic
failure modes, reflecting how modern LLM safety systems are built in practice.

