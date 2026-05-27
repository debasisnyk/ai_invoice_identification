# Gemini Function Calling Notes

---

# Core Concept

Gemini converts NATURAL LANGUAGE
into STRUCTURED FUNCTION PARAMETERS
based on the tool schema you provided.

Example:

User says:

"Show failed invoices from Germany above 5000"

Gemini converts it into:

{
    "country": "Germany",
    "min_amount": 5000
}

based on the tool definition/schema.

---

# Very Important

Gemini does NOT:
- execute Python
- read CSV
- run pandas
- access systems directly

Python does the real execution.

Gemini ONLY:
- understands language
- extracts intent
- chooses functions/tools
- creates structured parameters

---

# Function Calling Mental Model

Human Language
        ↓
Gemini Understanding
        ↓
Structured Parameters
        ↓
Python Function Execution
        ↓
Business Result

---

# Real Meaning Of Function Calling

Function calling is NOT:

"Gemini executes Python"

Function calling IS:

"Gemini REQUESTS Python to execute something"

---

# What tools=[invoice_tool] Does

config=types.GenerateContentConfig(
    tools=[invoice_tool]
)

This tells Gemini:

"You are allowed to use this function/tool"

Without this:
- Gemini behaves like normal chatbot
- Gemini does not know your function exists

With this:
- Gemini can generate function calls

---

# Tool Schema Purpose

The tool schema teaches Gemini:
- function name
- function purpose
- required parameters
- parameter data types

Example:

{
    "name": "get_failed_invoices",
    "parameters": {
        "country": "STRING",
        "min_amount": "INTEGER"
    }
}

---

# Important Architecture Concept

Gemini handles:
- natural language
- reasoning
- parameter extraction
- orchestration

Python handles:
- business logic
- filtering
- CSV/Excel
- APIs
- calculations
- automation

Best practice:
Use Python for deterministic logic.
Use Gemini for understanding language.

---

# Understanding This Line

function_call = response.candidates[0].content.parts[0].function_call

This navigates inside Gemini response object.

Response structure:

response
└── candidates[0]
    └── content
        └── parts[0]
            └── function_call

The final function_call contains:

{
    "name": "get_failed_invoices",
    "args": {
        "country": "Germany",
        "min_amount": 5000
    }
}

---

# Why candidates[0] ?

Because candidates is a LIST.

Example:

[
   candidate1,
   candidate2
]

[0] means first item.

---

# Why parts[0] ?

Because Gemini responses can contain:
- text
- function calls
- images
- multiple response parts

So responses are split into PARTS.

---

# Important Learning

Gemini response is NOT plain text.

It is a structured object similar to:
- JSON
- REST API responses
- ServiceNow responses
- SAP API payloads

Learning to navigate nested objects is a critical backend/API skill.

---

# Pandas Filtering Concept

Example:

df[
    (df["country"] == "Germany")
    &
    (df["amount"] > 5000)
]

Meaning:

"Give rows where:
- country is Germany
AND
- amount > 5000"

---

# Why df[ condition ] ?

Outer df:
- filters dataframe rows

Inner df:
- creates conditions

Example:

df["country"] == "Germany"

returns:

True
True
False
True

Then outer df keeps only True rows.

---

# Golden Rule

LLMs are best for:
- understanding
- reasoning
- language interpretation

Python is best for:
- execution
- calculations
- business rules
- automation
- APIs
- filtering

Do NOT waste LLM tokens on deterministic logic.

---

# Current Project Flow

User Prompt
    ↓
Gemini understands request
    ↓
Gemini creates function call
    ↓
Python extracts parameters
    ↓
Python executes function
    ↓
CSV gets filtered
    ↓
Result returned

---

# Future Real Enterprise Examples

This same architecture can later connect to:
- SAP
- ServiceNow
- UiPath
- SQL databases
- APIs
- Excel reports
- Power BI pipelines

The architecture remains the same.

---

# Most Important Sentence

Gemini converts NATURAL LANGUAGE
into STRUCTURED FUNCTION PARAMETERS
based on the tool schema you provided.