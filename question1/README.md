# Technical Debt Diagnosis

## 1. Identification of Hidden Technical Debt Categories

Based on the six sources of hidden technical debt in ML systems, here is the diagnosis for each scenario:

*   **(a) Entanglement (CACE):** Changing the "estimated delivery time" feature hurt the "favorite restaurants" feature because "Changing Anything Changes Everything"[cite: 1]. In ML systems, altering one feature can silently shift the entire model's behavior[cite: 1].
*   **(b) Undeclared Consumers:** The marketing dashboard team is an undeclared consumer because they are silently consuming the model's output via a shared table[cite: 1]. This creates invisible dependencies that can block safe changes[cite: 1].
*   **(c) Configuration & Glue-Code Debt:** The chain of 14 undocumented shell scripts is a classic example of this debt, where systems evolve into tangled "pipeline jungles" without a single source of truth for orchestration or configuration[cite: 1].

---

## 2. Proposed Mitigation

**Mitigating (c) Configuration & Glue-Code Debt using MLflow**

To resolve the tangled pipeline jungle of undocumented shell scripts, the team should implement **Experiment Tracking with MLflow**[cite: 1]. 

As taught in class that "Experiment tracking directly counters Configuration Debt"[cite: 1]. By replacing the undocumented scripts with MLflow, the team can systematically log parameters, metrics, and artifacts for every single run[cite: 1]. This establishes a clear, trackable history (via the MLflow Tracking Server and Backend Store) so that every model training execution has a single source of truth, rather than relying on scattered scripts[cite: 1].
