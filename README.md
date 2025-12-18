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
3. Demonstrates how early safety checks reduce downstream hallucinations

The focus is on **system-level AI safety**, not just model accuracy.

---

## Problem Statement
LLM applications frequently trust retrieved documents without verifying 
intent or safety. Malicious instructions hidden in retrieved text can 
override system behavior and cause hallucinations. Post-generation 
filtering alone is insufficient.

**Goal:**  
Build a modular safety layer that detects poisoning *before* inference and 
measures hallucination reduction *after* inference.


---

## Threat Model
### Attacks Covered
- Prompt Injection
- Instruction Override
- Context / Document Poisoning
- Retrieval Poisoning (RAG-specific)

### Out of Scope
- Model weight poisoning
- Supply-chain attacks
- Adversarial token perturbations

---

## System Architecture
User Query
↓
Retriever (Embedding-based)
↓
Retrieved Context
↓
Poisoning Detection Layer
├── Prompt Injection Detector
├── Intent Mismatch Detector
└── Token Anomaly Detector
↓ (if safe)
LLM Generation (simulated)
↓
Hallucination Verification (NLI-based)
↓
Final Answer + Safety Signal

---

## Methodology

### 1. Poisoning Detection (Pre-generation)
A **multi-layer defense** is used:

- **Prompt Injection Detector**
  - Flags instruction-override language
- **Intent Mismatch Detector**
  - Uses sentence embeddings to detect semantic divergence between query 
and context
- **Token Anomaly Detector**
  - Detects abnormal imperative or system-level language

If any detector triggers, generation is blocked.

---

### 2. Retrieval-Augmented Generation (RAG Simulation)
- Documents are embedded using Sentence-BERT
- Query–document similarity is computed via cosine similarity
- The most relevant document is retrieved
- The retrieval layer is modular and can be replaced with FAISS in 
production

---

### 3. Hallucination Detection (Post-generation)
- Uses a Natural Language Inference (NLI) model
- Checks whether the generated answer is **entailed** by the retrieved 
context
- Non-entailed responses are flagged as hallucinations

---

## Evaluation
The system is evaluated qualitatively by comparing:

- **Without poisoning detection:** hallucinations observed
- **With poisoning detection:** hallucinations reduced by blocking 
malicious context

This demonstrates that many hallucinations originate from poisoned inputs 
rather than model limitations.

---


## Technologies Used
- Python
- HuggingFace Transformers
- Sentence-BERT
- Natural Language Inference (NLI)
- Retrieval-Augmented Generation (RAG)
- AI Safety Techniques

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

## Author
Built as an AI safety and systems-focused project for advanced software 
engineering and machine learning internships.
