import pymysql
from pymysql import cursors


def create_connection(host="localhost", user="root", password="mysql", database="recipe", port=3306):
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port, cursorclass=cursors.DictCursor)
        print("Connection to MySQL DB successful")
        return connection
    except Exception as e:
        print(f"Error creating database connection: {e}")
        raise pymysql.Error(e)


def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, args=args)
            connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"The error '{e}' occurred")
            raise pymysql.Error(e)


def execute_read_query(connection, query):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"The error '{e}' occurred")
            raise pymysql.Error(e)


def set_up_database(host="localhost", user="root", password="mysql", port=3306):
    connection = pymysql.connect(host=host, user=user, password=password, port=port)
    execute_query(connection, "DROP DATABASE IF EXISTS recipe;")
    execute_query(connection, "CREATE DATABASE recipe;")
    connection = create_connection(database="recipe")
    execute_query(connection, """
    CREATE TABLE category(
        category_id INT PRIMARY KEY AUTO_INCREMENT,
	    category_name VARCHAR(64) NOT NULL UNIQUE,
	    photo VARCHAR(128) NOT NULL);
    """)
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Lunch", "assets/lunch.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Breakfast", "assets/breakfast.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Dinner", "assets/dinner.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Vegan", "assets/vegan.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Dessert", "assets/dessert.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Drinks", "assets/drinks.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Lunch 2", "assets/lunch.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Breakfast 2", "assets/breakfast.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Dinner 2", "assets/dinner.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Vegan 2", "assets/vegan.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Dessert 2", "assets/dessert.png"))
    execute_query(connection, "INSERT INTO category(category_name, photo) VALUES (%s, %s);", ("Drinks 2", "assets/drinks.png"))
