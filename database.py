import psycopg2
from config import settings
from psycopg2 import sql


connection = psycopg2.connect(
    dbname=settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
)

cursor = connection.cursor()


#Просмотр версии
def display_version():

    version_sql = sql.SQL("SELECT version();")

    with connection.cursor() as cursor:
        cursor.execute(
            version_sql
        )
        connection.commit()
        version = f"BD Version: {cursor.fetchone()}"
        return version


#Создание таблицы
def create_table(table_name):

    create_table_sql = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100),
            password VARCHAR(100)
        );
    """).format(sql.Identifier(table_name))
        
    with connection.cursor() as cursor:
        cursor.execute(
            create_table_sql
        )
    print(f"Table {table_name} created")

        
        
#Ввод в таблицу
def insert_data(table_name, name, age, mail, password):

    insert_sql = sql.SQL("INSERT INTO {} (name, age, email, password) VALUES (%s, %s, %s, %s);").format(sql.Identifier(table_name))

    with connection.cursor() as cursor:
        cursor.execute(
        insert_sql, (name, age, mail, password)
    )
    connection.commit()
    print(f"INSERT INTO ({table_name}): {name}, {age}, {mail}, {password}")


#Отображение таблицы
def display_table(table_name):

    display_sql = sql.SQL("SELECT * FROM {};").format(sql.Identifier(table_name))

    with connection.cursor() as cursor:
        cursor.execute(
            display_sql
        )
        data = f"DATA FROM DATABASE {table_name}: {cursor.fetchall()}"
        print(data)

    
        
#Изменение таблицы
def update_table(table_name, age, name):

    update_sql = sql.SQL("""
        UPDATE {}
        SET возраст = %s
        WHERE имя = %s;
    """).format(sql.Identifier(table_name))

    with connection.cursor() as cursor:
        cursor.execute(
            update_sql, (age, name)
    )


#Очистка таблицы
def clear_table(table_name):

    clear_sql = sql.SQL("DELETE FROM {};").format(sql.Identifier(table_name))

    with connection.cursor() as cursor:
        cursor.execute(
            clear_sql
        )

# Изменение пароля
def update_password_in_table(table_name, name, old_password, new_password):
    
    change_pass_sql = sql.SQL("UPDATE {} SET password = %s WHERE name = %s AND PASSWORD = %s;").format(sql.Identifier(table_name))
    
    print(f"Attempting to update password for user: {name} with old password: {old_password}")
    
    with connection.cursor() as cursor:
        cursor.execute(
            change_pass_sql, (new_password, name, old_password)
        )
        connection.commit()

        if not cursor.rowcount > 0:
            print(f"Пароль пользователя {name} был изменен!")
        else:
            print(f"Не получилось изменить пароль")

    

    

if __name__== "__main__":

    new_table_name = 'vpn_user2'
    print(display_version())

    name = 'Иллидан'
    age =  30
    mail = 'pilv2002@gmail.com'
    
    user_list = [name, age, mail]
    
    create_table(new_table_name)
    #clear_table(new_table_name)
    #insert_data(new_table_name, 'Иллидан', 22, 'pilv2002@gmail.com', '63613')
    update_password_in_table(new_table_name, 'Иллидан', '09244', '63613')
    display_table(new_table_name)
