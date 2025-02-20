import psycopg2
from psycopg2 import sql

create_table_sql = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100)
    );
""")
print(create_table_sql)

table_name = 'new_table'

create_table_sql = create_table_sql.format(sql.Identifier(table_name))
print("=======================")

print(create_table_sql)

display_sql = sql.SQL("SELECT * FROM {};").format(sql.Identifier('new_table'))

display_test = sql.SQL("SELECT * FROM {};")



display = display_test.format(sql.Identifier(table_name))
print(display_sql)
print('=====================')
print(display)



insert_sql = sql.SQL("INSERT INTO {} (name, age, email) VALUES (%s, %s, %s);")
print(insert_sql)
insert_sql = insert_sql.format(sql.Identifier(table_name))

print(insert_sql)