import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="deutschmate",
        user="postgres",
        password="postgres",
        port=5433
    )

    print("Connected successfully!")

    conn.close()

except Exception as e:
    print(e)