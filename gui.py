from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from scanner.security_scan import run_security_scan
from scanner.style_scan import run_style_scan
from ai_helper.explainer import explain_issue
from ai_helper.ai_chat import ask_ai

# -----------------------------
# Dark Theme Colors
# -----------------------------
BG_MAIN = "#0f172a"
BG_PANEL = "#1f2933"
BG_INPUT = "#111827"

FG_TEXT = "#e5e7eb"
FG_MUTED = "#9ca3af"

ACCENT_BLUE = "#3b82f6"
ACCENT_GREEN = "#22c55e"
ACCENT_RED = "#ef4444"

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("AI-Assisted Secure Code Review")
root.geometry("1000x720")
root.configure(bg=BG_MAIN)



# -----------------------------
# Header
# -----------------------------
header = tk.Frame(root, bg=BG_PANEL, height=60)
header.pack(fill="x")

title = tk.Label(
    header,
    text="AI-Assisted Secure Code Review",
    bg=BG_PANEL,
    fg=FG_TEXT,
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=15)

# -----------------------------
# File Selection Panel
# -----------------------------
file_panel = tk.Frame(root, bg=BG_MAIN)
file_panel.pack(fill="x", padx=20, pady=10)

file_path_var = tk.StringVar(value="No file selected")

file_label = tk.Label(
    file_panel,
    textvariable=file_path_var,
    bg=BG_MAIN,
    fg=FG_MUTED,
    font=("Segoe UI", 10)
)
file_label.pack(side="left", padx=5)

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if path:
        file_path_var.set(path)

browse_btn = tk.Button(
    file_panel,
    text="Browse Python File",
    bg=ACCENT_BLUE,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=browse_file
)
browse_btn.pack(side="right", padx=5)

scan_btn = tk.Button(
    file_panel,
    text="Scan File",
    bg=ACCENT_GREEN,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=lambda: scan_file()
)
scan_btn.pack(side="right", padx=5)

# -----------------------------
# Output Box
# -----------------------------
output_frame = tk.Frame(root, bg=BG_MAIN)
output_frame.pack(fill="both", expand=True, padx=20, pady=10)

output_box = tk.Text(
    output_frame,
    bg=BG_INPUT,
    fg=FG_TEXT,
    insertbackground=FG_TEXT,
    font=("Consolas", 10),
    wrap="word"
)
output_box.pack(fill="both", expand=True)

# -----------------------------
# Scan Logic
# -----------------------------
def scan_file():
    output_box.delete("1.0", "end")

    file_path = file_path_var.get()
    if not Path(file_path).exists():
        messagebox.showerror("Error", "Please select a valid Python file.")
        return

    output_box.insert("end", "=== Secure Code Review Report ===\n\n")

    # Security scan
    security_report = run_security_scan(file_path)
    security_issues = security_report.get("results", [])

    output_box.insert("end", "--- Security Issues ---\n\n")
    if not security_issues:
        output_box.insert("end", "No security issues found.\n\n")
    else:
        for i, issue in enumerate(security_issues, start=1):
            explanation = explain_issue(issue["test_id"], issue)
            output_box.insert("end", f"[{i}] {issue['test_id']} - {issue['test_name']}\n")
            output_box.insert("end", f"Severity   : {issue['issue_severity']}\n")
            output_box.insert("end", f"Confidence : {issue['issue_confidence']}\n")
            output_box.insert("end", f"Line       : {issue['line_number']}\n")
            output_box.insert("end", f"Code       : {issue['code'].strip()}\n")
            output_box.insert("end", f"Why        : {explanation['why']}\n")
            output_box.insert("end", f"Risk       : {explanation['risk']}\n")
            output_box.insert("end", f"Fix        : {explanation['fix']}\n\n")

    # Style scan
    style_issues = run_style_scan(file_path)

    output_box.insert("end", "--- PEP8 / Style Issues ---\n\n")
    if not style_issues:
        output_box.insert("end", "No PEP8 issues found.\n")
    else:
        for i, issue in enumerate(style_issues, start=1):
            code = issue["message"].split()[0]
            explanation = explain_issue(code)
            output_box.insert(
                "end",
                f"[{i}] Line {issue['line']}, Col {issue['column']}\n"
                f"Message : {issue['message']}\n"
                f"Why     : {explanation['why']}\n"
                f"Risk    : {explanation['risk']}\n"
                f"Fix     : {explanation['fix']}\n\n"
            )

    output_box.see("end")

# -----------------------------
# AI Assistant Panel
# -----------------------------
ai_panel = tk.Frame(root, bg=BG_PANEL)
ai_panel.pack(fill="x", padx=20, pady=10)

ai_label = tk.Label(
    ai_panel,
    text="Ask the AI Assistant (plain English)",
    bg=BG_PANEL,
    fg=FG_TEXT,
    font=("Segoe UI", 11, "bold")
)
ai_label.pack(anchor="w", pady=5)

ai_input = tk.Entry(
    ai_panel,
    bg=BG_INPUT,
    fg=FG_TEXT,
    insertbackground=FG_TEXT,
    font=("Segoe UI", 10)
)
ai_input.pack(fill="x", padx=5, pady=5)

def explain_with_ai():
    question = ai_input.get().strip()
    if not question:
        return

    output_box.insert("end", "\n--- AI Assistant ---\n")
    output_box.insert("end", f"You: {question}\n")

    response = ask_ai(question)
    output_box.insert("end", f"Assistant: {response}\n")
    output_box.see("end")

ai_btn = tk.Button(
    ai_panel,
    text="Explain",
    bg=ACCENT_BLUE,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=explain_with_ai
)
ai_btn.pack(anchor="e", padx=5, pady=5)

# -----------------------------
# Start App
# -----------------------------
root.mainloop()
