import pymysql

def get_database_info():
    print("Enter your database credentials:")
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def connect_to_database(username, password):
    try:
        connection = pymysql.connect(
            host='localhost',
            user=username,
            password=password,
            database='info_group',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to the database.")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def save_database_info_to_file(connection):
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM db_clients"
                cursor.execute(sql)
                data = cursor.fetchall()

                with open("database_info.txt", "w") as f:
                    for row in data:
                        f.write(str(row) + "\n")

            print("Database information saved to database_info.txt")
        except pymysql.Error as e:
            print(f"Error executing SQL query: {e}")
    else:
        print("Cannot save database information. Not connected to the database.")

def main():
    username, password = get_database_info()
    connection = connect_to_database(username, password)
    save_database_info_to_file(connection)

if __name__ == "__main__":
    main()
