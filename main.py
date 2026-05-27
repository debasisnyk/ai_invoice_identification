import pandas as pd

# -----------------------------
# Read CSV file
# -----------------------------

df = pd.read_csv("invoices.csv")

# -----------------------------
# Function to get Invoices with status "failed" for a specific country and minimum amount
# -----------------------------

def get_failed_invoices(country, min_amount):

    filtered_df = df[
        (df["country"].str.lower() == country.lower())
        & (df["status"].str.lower() == "failed")
        & (df["amount"] > min_amount)
    ]

    return filtered_df

# -----------------------------
# Test function
# -----------------------------

result = get_failed_invoices("Germany", 5000)

print(result)