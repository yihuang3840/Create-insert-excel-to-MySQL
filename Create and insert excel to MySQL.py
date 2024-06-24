import pandas as pd
import mysql.connector

# Read Excel
df = pd.read_excel("C:/Users", keep_default_na = False)


# MySQL DB connection
conn = mysql.connector.connect(
  host="host IP",
  user="User ID",
  password="Password",
  database='Database name')

cursor = conn.cursor()

# Create Table
cursor.execute('''
            CREATE TABLE model_codes_mfg(
            model_code int(11),
            product_name text,
            bartender_file text,
            product_rev char(2),
            006_rev char(2),
            105_rev char(2),
            012_rev char(2),
            ECO text,
            datetime timestamp,
            status tinyint(1),
            Product_GPN varchar(200)
            )''')

# Insert data to Table
for i, row in df.iterrows():
    cursor.execute("""
        INSERT INTO model_codes_mfg (model_code, product_name, bartender_file, product_rev, 006_rev, 105_rev, 012_rev, ECO, datetime, status, Product_GPN)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row['model_code'], row['product_name'],row['bartender_file'], row['product_rev'],row['006_rev'], row['105_rev'],row['012_rev'], row['ECO'],row['datetime'],row['status'], row['Product_GPN']))

# Connection close
conn.commit()
cursor.close()
conn.close()