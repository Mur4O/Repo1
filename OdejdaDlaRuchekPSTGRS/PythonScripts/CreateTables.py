from main import *

path_to_tables = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/Tables'
table_names, file_names = files_in_path(path_to_tables)
path_to_query = '/Users/yarik/PycharmProjects/Repo1/OdejdaDlaRuchekPSTGRS/PythonScripts/CreateOrDrop.txt'
schema = 'dbo'

queries = create_queries(path_to_tables, path_to_query, table_names, schema, file_names)
# print(queries[4])

conn = psycopg.connect(f"postgresql://postgres@sqlserver/carservice3isp931")
cursor = conn.cursor()

for q in queries:
    # print(q)
    cursor.execute(q)
    conn.commit()

cursor.close()
conn.close()
