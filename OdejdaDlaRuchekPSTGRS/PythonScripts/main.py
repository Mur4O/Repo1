import os
import psycopg

def files_in_path(path):
    dir_list = os.listdir(path)
    fin_list = []
    for file in dir_list:
        file = file[:-4]
        fin_list.append(file)
    return fin_list, dir_list

def read_file(path):
    with open(path, 'r') as f:
        arr = f.readlines()
        fin = ' '.join(arr)
    return fin

def create_queries(path_to_files, path_to_query, names, shema, file_names):
    return_list = []
    i = 0

    for name in names:
        query = read_file(path_to_query)
        path_to_file = f'{path_to_files}/{file_names[i]}'
        sub_query = read_file(path_to_file)

        query = query.format(name, sub_query, shema)
        return_list.append(query)
        i += 1

    return return_list

def create_tables(conn, cursor):
    path_to_tables = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/Tables'
    table_names, file_names = files_in_path(path_to_tables)
    path_to_query = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/PythonScripts/CreateOrDrop.txt'
    schema = 'dbo'

    queries = create_queries(path_to_tables, path_to_query, table_names, schema, file_names)
    # print(queries[4])

    for q in queries:
        # print(q)
        cursor.execute(q)
        conn.commit()


def PreDeployment(conn, cursor):
    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/DB/AllFKs.sql'

    with open(path, 'r') as fp:
        lines = fp.readlines()

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
        # print(query)

        cursor.execute(query)
    conn.commit()

def PostDeployment(conn, cursor):
    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/Constraints/FKs.sql'

    with open(path, 'r') as fp:
        lines = fp.readlines()

    query = " ".join(lines)

    cursor.execute(query)
    conn.commit()
