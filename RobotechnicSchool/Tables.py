import os
import psycopg

def CreateTables():
    path_to_folder = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/Create table'

    conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")

    cursor = conn.cursor()

    i: int = -1
    dir_list = os.listdir(path_to_folder)
    for var in dir_list:
        i += 1

        path = f'{path_to_folder}/{dir_list[i]}'

        with open(path, 'r') as fp:
            lines = fp.readlines()

        query = " ".join(lines)

        cursor.execute(query)

        # for row in cursor:
        #     print(row)

        conn.commit()
    cursor.close()
    conn.close()