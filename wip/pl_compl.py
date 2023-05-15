import pandas as pd
import numpy as np
import json

with open('filename.txt', 'r') as f:
    filename = f.read()
print(f'../csvs/{filename}.csv')
df = pd.read_csv(f'../csvs/{filename}.csv')

def convert_to_iso_date(date_str):
    # Convert date from MM/DD/YYYY to ISO 8601 format YYYY-MM-DD
    month, day, year = date_str.split('/')
    iso_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return iso_date

# Select the financial records and assign column names for df_records
df_records = df.iloc[6:]
df_records.columns = df.iloc[5]
df_info = df.iloc[:4, :2]
df_info.columns = ['Name', 'Type']


# Generate JSON object for df_records
def generate_json_object(df_records):
    data = {
       "company_name": df_info.iloc[0, 1],
        "accounting_method": df_info.iloc[1, 1],
        "start_date": df_info.iloc[2, 1],
        "end_date": df_info.iloc[3, 1],
        "income": [],
        "expenses": []
    }

    for _, row in df_records.iterrows():
        record_type = row['record_type']
        category = row['category']
        description = row['description']
        amount = float(row['amount'])

        record = {
            "category": category,
            "description": description,
            "amount": amount
        }

        if record_type == 'income':
            data['income'].append(record)
        elif record_type == 'expense':
            data['expenses'].append(record)

    return data

# Convert df_records to JSON object
json_data = json.dumps(generate_json_object(df_records), indent=4)

print(df_records)
print(df_info)

with open('../json/sample.json', 'w') as json_file:
    json_file.write(json_data)
