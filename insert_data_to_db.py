import sqlite3
from sqlite3 import Error
#https://www.sqlitetutorial.net/sqlite-python/
from readlines import read_data

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

def insertmany_data(conn, data):
    sql = '''INSERT INTO bme280_data (datetime_int, temperature, pressure, humidity)
             VALUES (strftime('%s', ?), ?, ?, ?);'''
    cur = conn.cursor()
    cur.executemany(sql, data)
    return cur.lastrowid


if __name__ == '__main__':
    database = r"home_temp.db"
    wtf = read_data('weather_BME280_sensor_data.txt')
    print(wtf[0], "...", "\n", "...", len(wtf), "...", "\n", "...",  wtf[-1])
    sql = '''INSERT INTO bme280_data (datetime_int, temperature, pressure, humidity)
             VALUES (strftime('%s', ?), ?, ?, ?);'''
    # create a database connection
    conn = sqlite3.connect("home_temp.db")
    cur = conn.cursor()

    cur.executemany(sql, wtf)
    conn.commit()
    conn.close()
