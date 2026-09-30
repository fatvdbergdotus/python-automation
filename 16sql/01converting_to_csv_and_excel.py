import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Retrieve the data from the 'ips' table ordered by ASN in a DataFrame
df = pd.read_sql_query("SELECT * FROM ips ORDER BY asn", conn)
print(df)

# Close the connection
conn.close()
