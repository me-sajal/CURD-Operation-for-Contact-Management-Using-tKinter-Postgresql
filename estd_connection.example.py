import psycopg2


def estd_connections():
    conn = psycopg2.connect(
        database='',
        user='',
        password='',
        host='',
        port=5432
    )

    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor
