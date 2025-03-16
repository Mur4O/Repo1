from main import *

conn = psycopg.connect(f"postgresql://postgres@sqlserver/carservice3isp931")
cursor = conn.cursor()

PreDeployment(conn, cursor)
create_tables(conn, cursor)
PostDeployment(conn, cursor)

cursor.close()
conn.close()