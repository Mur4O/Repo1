import os
import psycopg

path_to_folder = '/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/Create table'

i = 0
dir_list = os.listdir(path_to_folder)
for var in dir_list:
    path = f'/Users/yarik/PycharmProjects/Repo1/RobotechnicSchool/Create table/{dir_list[i]}'

    with open(path, 'r') as fp:
        lines = fp.readlines()

    query = " ".join(lines)
    print(query)

    # try:
    conn = psycopg.connect(f"postgresql://postgres@sqlserver/robotechnicdb")
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()


    i+=1