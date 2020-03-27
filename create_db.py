import sqlite3
from sqlite3 import Error
#https://www.sqlitetutorial.net/sqlite-python/
#https://datatofish.com/create-database-python-using-sqlite3/

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def main():
    database = r"./home_temp.db"

    sql_create_data_table = """CREATE TABLE IF NOT EXISTS bme280_data (
                                key INTEGER PRIMARY KEY,
                                datetime_int INTEGER NOT NULL,
                                temperature INTEGER,
                                pressure INTEGER,
                                humidity INTEGER,
                            );"""

    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create data table
        create_table(conn, sql_create_data_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    #main()
    conn = sqlite3.connect('home_temp.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

    # Create table - bme280_data
    sql_create_data_table = """CREATE TABLE IF NOT EXISTS bme280_data (
                                key INTEGER PRIMARY KEY, 
                                datetime_int INTEGER, 
                                temperature INTEGER, 
                                pressure INTEGER, 
                                humidity INTEGER
                                );"""
    if conn is not None:
        # create data table
        create_table(conn, sql_create_data_table)
    else:
        print("Error! cannot create the database connection.")

    sql_create_test_table = """CREATE TABLE IF NOT EXISTS test_data (
                                datetime_int INTEGER, 
                                temperature INTEGER, 
                                pressure INTEGER, 
                                humidity INTEGER
                                );"""
    if conn is not None:
        # create data table again
        create_table(conn, sql_create_test_table)
    else:
        print("Error! cannot create the database connection.")
