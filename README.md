# AI Invoice Assistant using Gemini Function Calling

A beginner-friendly AI automation project built with Python and the Gemini API to demonstrate how function calling works in real-world enterprise-style workflows.

This project shows how Gemini can convert natural language requests into structured function parameters, while Python performs the actual business logic and data processing.

---

# Project Goal

The goal of this project is to understand:

- Gemini function calling
- Tool/function schemas
- Natural language to structured parameter conversion
- Python function execution
- CSV data filtering using pandas
- AI + automation architecture fundamentals

---

# Example Workflow

User asks:

```text
Show failed invoices from Germany above 5000
```

Gemini converts this into structured parameters:

```json
{
    "country": "Germany",
    "min_amount": 5000
}
```

Python then:
- reads invoice CSV data
- filters matching records
- returns the result

---

# Core Learning Concept

> Gemini converts NATURAL LANGUAGE into STRUCTURED FUNCTION PARAMETERS based on the tool schema you provided.

Gemini does NOT:
- execute Python
- filter CSV files
- run pandas logic

Python handles all actual execution and business logic.

Gemini is responsible for:
- understanding user intent
- selecting tools/functions
- extracting structured parameters

---

# Technologies Used

- Python
- Gemini API
- pandas
- python-dotenv
- VS Code

---

# Project Structure

```text
invoice_ai_project/
│
├── main.py
├── invoices.csv
├── NOTES.md
├── requirements.txt
├── .env
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Add Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 4. Run Project

```bash
python main.py
```

---

# Example Prompts

```text
Show failed invoices from Germany above 5000
```

```text
Find failed invoices in USA over 10000
```

```text
Show failed French invoices above 1000
```

---

# Example Architecture

```text
Human Language
        ↓
Gemini Understanding
        ↓
Structured Parameters
        ↓
Python Function Execution
        ↓
Business Result
```

---

# Future Improvements

Possible future enhancements:

- Multiple function/tools support
- ServiceNow integration
- SAP integration
- SQL database support
- UiPath orchestration
- Email notifications
- Streamlit web UI
- AI agent workflows

---

# Learning Notes

Additional technical learning notes are documented in:

```text
NOTES.md
```

---

# Author

Debasis Nayak

Learning journey from RPA & Automation into AI Engineering and AI-powered enterprise automation.
