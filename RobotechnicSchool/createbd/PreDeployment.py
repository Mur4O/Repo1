import os
import psycopg

path = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/createbd/PreDeployment.sql'
conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")

with open(path, 'r') as fp:
    lines = fp.readlines()

cursor = conn.cursor()

query = " ".join(lines)

cursor.execute(query)
for row in cursor:
    print(row)

conn.commit()

cursor.close()
conn.close()

