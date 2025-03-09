import os
import psycopg

def PreDeployment():
    path = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/createbd/PreDeployment.sql'

    conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")

    with open(path, 'r') as fp:
        lines = fp.readlines()

    cursor = conn.cursor()

    query = " ".join(lines)

    rows = []
    cursor.execute(query)
    for row in cursor:
        rows.append(row)
    # print(rows)

    i: int = -1
    for element in rows:
        i += 1
        query = f'alter table dbo.{rows[i][0]} drop constraint {rows[i][1]}'
        print(query)

        cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()