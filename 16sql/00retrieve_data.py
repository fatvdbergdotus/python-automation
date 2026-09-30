import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Retrieve the first 5 rows of data from the 'ips' table ordered by ASN
cursor.execute("SELECT * FROM ips ORDER BY asn LIMIT 0,5")
rows = cursor.fetchall()
print("address,domain,asn")
for row in rows:
    print(row[0], row[1], row[2])

print(40*"=")

# Retrieve the first 5 rows of data from the 'ips' table columns address and ASN
cursor.execute("SELECT address, asn FROM ips LIMIT 0,5")
rows = cursor.fetchall()
print("address,asn")
for row in rows:
    print(row[0], row[1])

print(40*"=")

# Retrieve the first 5 rows of data from the 'ips' table columns domain and ASN where ASN>120
cursor.execute("SELECT domain, asn FROM ips WHERE asn>120 LIMIT 0,5")
rows = cursor.fetchall()
print("domain,asn")
for row in rows:
    print(row[0], row[1])

print(40*"=")

# Retrieve the first 5 rows of data from the 'ips' table columns domain and ASN where ASN>120 and domain like laco
cursor.execute("SELECT domain, asn FROM ips WHERE asn>120 AND domain LIKE '%laco%' LIMIT 0,5")
rows = cursor.fetchall()
print("domain,asn")
for row in rows:
    print(row[0], row[1])

# Close the connection
conn.close()