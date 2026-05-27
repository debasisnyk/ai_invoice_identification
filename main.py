from google import genai
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
# Ask user input
# -----------------------------

user_prompt = input("Ask something: ")

# -----------------------------
# Send prompt to Gemini
# -----------------------------

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt
)

# -----------------------------
# Print response
# -----------------------------

print("\nGemini Response:\n")

print(response.text)