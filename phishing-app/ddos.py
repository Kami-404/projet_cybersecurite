import pymysql
import threading
import time

DB_HOST = 'localhost'
DB_USER = 'sebastien1'
DB_PASSWORD = 'ggopt'
DB_NAME = 'info_group'

def connect_to_database():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def perform_query():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id`, `first_name`, `last_name`, `email`, `gender`, `phone`, `iban`, `current_account` FROM `db_clients`")
                result = cursor.fetchall()
                print(f"Fetched {len(result)} records")
        except pymysql.Error as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()

def ddos_simulation(num_bots):
    threads = []
    for _ in range(num_bots):
        t = threading.Thread(target=perform_query)
        t.start()
        threads.append(t)
        time.sleep(0.1)

    for t in threads:
        t.join()

if __name__ == "__main__":
    num_bots = int(input("Enter the number of botnets to simulate: "))
    ddos_simulation(num_bots)
