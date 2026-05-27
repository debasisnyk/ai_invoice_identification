from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# -----------------------------
# Load environment variables
# -----------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Create Gemini client
# -----------------------------

client = genai.Client(api_key=api_key)

# -----------------------------
# TOOL DECLARATION
# -----------------------------

invoice_tool = {
    "function_declarations": [
        {
            "name": "get_failed_invoices",
            "description": "Get failed invoices from a country above a minimum amount",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "country": {
                        "type": "STRING",
                        "description": "Country name"
                    },
                    "min_amount": {
                        "type": "INTEGER",
                        "description": "Minimum invoice amount"
                    }
                },
                "required": ["country", "min_amount"]
            }
        }
    ]
}

# -----------------------------
# User input
# -----------------------------

user_prompt = input("Ask something: ")

# -----------------------------
# Send to Gemini
# -----------------------------

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,

    config=types.GenerateContentConfig(
        tools=[invoice_tool]
    )
)

# -----------------------------
# Print RAW response
# -----------------------------

print(response)