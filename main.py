from google import genai
from google.genai import types
from dotenv import load_dotenv
import pandas as pd
import os

# -----------------------------Load environment variables

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# -----------------------------Create Gemini client

client = genai.Client(api_key=api_key)

# -----------------------------Read CSV

df = pd.read_csv("invoices.csv")

# -----------------------------Python Function

def get_failed_invoices(country, min_amount):

    filtered_df = df[
        (df["country"].str.lower() == country.lower())
        &
        (df["status"].str.lower() == "failed")
        &
        (df["amount"] > min_amount)
    ]

    return filtered_df.to_dict(orient="records")

# -----------------------------Tool Declaration

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

# -----------------------------User Prompt

user_prompt = input("Ask something: ")

# -----------------------------Send To Gemini

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=user_prompt,

    config=types.GenerateContentConfig(
        tools=[invoice_tool]
    )
)

# -----------------------------Extract Function Call
# Here Gemini converts natural language into structured parameters
function_call = response.candidates[0].content.parts[0].function_call

# -----------------------------Print Gemini Decision

print("\nGemini wants to call:\n")
print(function_call.name)
print(function_call.args)

# -----------------------------Execute Python Function

if function_call.name == "get_failed_invoices":

    country = function_call.args["country"]
    min_amount = function_call.args["min_amount"]

    result = get_failed_invoices(country, min_amount)

    print("\nPython Function Result:\n")
    print(result)