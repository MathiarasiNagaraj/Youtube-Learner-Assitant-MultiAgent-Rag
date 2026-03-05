SUMMARY_PROMPT = """
You are an expert technical educator.
Summarize the following YouTube transcript in structured bullet points:

Transcript:
{context}
"""

QUIZ_PROMPT = """
Generate exactly 5 multiple choice questions from the summary below.

Formatting rules:
- Each question must be on ONE single line.
- Format strictly as:
Q1. Question text? | A) option | B) option | C) option | D) option | Answer: correct option letter

Do not add explanations.
Do not add extra lines.
Do not use line breaks inside a question.

Summary:
{context}
"""