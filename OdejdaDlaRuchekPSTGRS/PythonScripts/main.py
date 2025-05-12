import os
import psycopg
import pandas as pd


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

    query = ("SET datestyle = 'ISO, DMY';")
    cursor.execute(query)

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
    # Поднимаем ограничения
    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/Constraints/FKs.sql'

    with open(path, 'r') as fp:
        lines = fp.readlines()

    query = " ".join(lines)

    cursor.execute(query)
    conn.commit()

    # Заполняем справочники
    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/DB/Inserts.sql'

    with open(path, 'r') as fp:
        lines = fp.readlines()

    query = " ".join(lines)

    cursor.execute(query)
    conn.commit()

    # Парсим данные из csv
    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/DataForInsert/client.csv'
    data = pd.read_csv(path, delimiter=';')
    tuples = [tuple(x) for x in data.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(data.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % ('dbo.client', 'firstname, lastname, patronymic, birthday, registrationdate, email, phone, gendercode, photopath')

    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1

    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/DataForInsert/service_a_import.csv'
    data = pd.read_csv(path, delimiter=';')
    tuples = [tuple(x) for x in data.to_numpy()]
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s)" % (
    'dbo.service', 'title, cost, durationinstock, description, discount')

    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1

    path = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/DataForInsert/clientservice_a_import.csv'
    data = pd.read_csv(path, delimiter=';')
    tuples = [tuple(x) for x in data.to_numpy()]
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s)" % (
        'dbo.clientservice', 'ClientId, ServiceId, StartTime, Comment')

    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()

















