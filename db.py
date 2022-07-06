import psycopg2
from psycopg2 import Error

dbName = "app.db"


def initDb():
    global cursor, connection
    try:
        connection = psycopg2.connect(password="1111",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="app")

        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE townsdata
                              (ID TEXT NOT NULL,
                               TOWN TEXT NOT NULL); '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def addData():
    try:
        connection = psycopg2.connect(password="1111",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="app")

        print("Database opened successfully")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO townsdata (ID, TOWN) VALUES ('ad', 'safasfa')"
        )

        connection.commit()
        print("Record inserted successfully")

        connection.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def getData():
    try:
        connection = psycopg2.connect(password="1111",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="app")

        print("Database opened successfully")
        cursor = connection.cursor()
        cursor.execute("SELECT ID, TOWN from townsdata")

        rows = cursor.fetchall()
        for row in rows:
            print("ID =", row[0])
            print("TOWN =", row[1], "\n")

        print("Operation done successfully")
        connection.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
