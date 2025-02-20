import pandas as pd
import requests
import datetime

# Load Excel file
excel_file = "data.xlsx"  # Ensure this file exists in the same directory
df = pd.read_excel(excel_file, sheet_name="Sheet1")

# API endpoint
api_url = "https://reqres.in/api/users"

# Log file
log_file = "log.txt"

# Function to log responses
def log_response(log_message):
    with open(log_file, "a") as log:
        log.write(f"{datetime.datetime.now()} - {log_message}\n")

# Process each user
for index, row in df.iterrows():
    payload = {
        "name": row["Name"],
        "email": row["Email"],
        "account_type": row["AccountType"]
    }

    # Send POST request
    response = requests.post(api_url, json=payload)

    if response.status_code == 201:
        user_data = response.json()
        user_id = user_data.get("id", "N/A")
        log_message = f" User {row['Name']} created successfully! ID: {user_id}"
    else:
        log_message = f" Failed to create {row['Name']}: {response.text}"

    print(log_message)
    log_response(log_message)

print(" Process completed! Check 'log.txt' for details.")
