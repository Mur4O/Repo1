import os
import psycopg

path = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/createbd/PreDeployment.sql'
conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")

with open(path, 'r') as fp:
    lines = fp.readlines()

cursor = conn.cursor()

query = " ".join(lines)

rows = []
cursor.execute(query)
for row in cursor:
    rows.append(row[0])
print(rows)

query = ""


conn.commit()
cursor.close()
conn.close()

