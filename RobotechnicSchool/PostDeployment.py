import os
import psycopg

def PostDeployment():
    path = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/createbd/PostDeployment.sql'

    conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")

    cursor = conn.cursor()

    with open(path, 'r') as f:
        list = f.readlines()

        query = ' '.join(list)

        cursor.execute(query)

        conn.commit()
    cursor.close()
    conn.close()