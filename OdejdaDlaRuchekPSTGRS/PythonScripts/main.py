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
    query = read_file(path_to_query)
    return_list = []
    i = 0

    for name in names:
        path_to_file = f'{path_to_files}/{file_names[i]}'
        sub_query = read_file(path_to_file)

        query = query.format(name, sub_query, shema)
        return_list.append(query)
        i += 1

    return return_list
