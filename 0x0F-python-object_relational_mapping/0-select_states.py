#!/usr/bin/python3
"""cript that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


def list_states(username, password, database):
    """defining to connect to database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    list_states(username, password, database)
