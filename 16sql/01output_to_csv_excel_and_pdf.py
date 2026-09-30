import sqlite3
import pandas as pd
from fpdf import FPDF

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Retrieve the data from the 'ips' table ordered by ASN in a DataFrame
df = pd.read_sql_query("SELECT * FROM ips ORDER BY asn", conn)

# Close the connection
conn.close()

# print the DataFrame to the console
print(df)

# Store the data in CSV and Excel files
df.to_csv('ips.csv', index=False)
df.to_excel('ips.xlsx', index=False)

# Store the data in a PDF table
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add table header
for col in df.columns:
    pdf.cell(40, 10, col, 1)
pdf.ln()

# Add table rows
for index, row in df.iterrows():
    for col in df.columns:
        pdf.cell(40, 10, str(row[col]), 1)
    pdf.ln()

pdf.output("ips.pdf")

