AI-Assisted Secure Code Review

A desktop GUI application for automated Python security and style analysis, enhanced with AI-powered explanations.

This project combines deterministic static analysis with language-model-based interpretation to improve the accessibility and clarity of secure code review.

Overview

The system performs:

Static security analysis using Bandit

PEP8 style checking

AI-powered explanation of findings (OpenAI API integration)

The goal is to bridge the gap between raw scanner output and human-readable security insight.

Key Features

Scan individual Python files for security vulnerabilities

Detect common insecure patterns (SQL injection, unsafe eval, insecure deserialization, weak hashing, etc.)

Identify PEP8 style violations

Generate plain-English explanations of detected issues

GUI-based workflow for ease of use

AI Integration

The GUI integrates an OpenAI API-powered assistant to provide clear, structured explanations of detected findings.

After static analysis completes, the AI layer can:

Translate scanner output into beginner-friendly explanations

Explain security risks and impact

Suggest secure coding improvements

The OpenAI API key is supplied via environment variable configuration.

This design preserves rule-based detection while enhancing interpretability through AI.

System Architecture

The system follows a layered approach:

File Input Layer

User selects a Python file via GUI.

Static Analysis Layer

Bandit performs security scanning.

PEP8 checks evaluate style compliance.

Processing Layer

Results are parsed and formatted.

AI Explanation Layer

Findings are optionally sent to the OpenAI API.

The model generates contextual explanations.

Output Layer

Results are displayed in the GUI.

This hybrid design separates deterministic detection from AI-based interpretation.

Evaluation

A controlled dataset was constructed to evaluate system performance.

Dataset:

10 intentionally vulnerable Python scripts

5 secure (clean) Python scripts

Metrics recorded:

True Positives (TP): 8

False Negatives (FN): 2

False Positives (FP): 0

True Negatives (TN): 5

Derived Metrics:

Precision: 1.00

Recall: 0.80

F1 Score: 0.89

The system demonstrated high precision and strong detection of API-level vulnerabilities.
Logical and business-layer vulnerabilities (e.g., missing authentication, improper validation) were not detected, reflecting a limitation of static pattern-based analysis.

Detailed report:

results/AI_Assisted_Secure_Code_Review_Evaluation.pdf

Raw experimental data:

results/evaluation_results.xlsx

Limitations

Limited dataset size (can be expanded for stronger statistical validity)

Reduced effectiveness for business logic vulnerabilities

Dependent on static analysis rules for detection

AI explanations do not replace formal verification

Future Improvements

Expand evaluation dataset (20+ vulnerable and clean samples)

Automate metric calculation

Compare against standalone Bandit CLI performance

Integrate semantic analysis for improved logical flaw detection

Add batch file scanning capability

Requirements

Python 3.x

Bandit

OpenAI Python SDK

Valid OpenAI API key (environment variable)

Research Motivation

Static analysis tools often produce technically correct but difficult-to-interpret output.
This project explores whether combining deterministic scanning with AI explanation can improve clarity and usability while preserving structured detection.
