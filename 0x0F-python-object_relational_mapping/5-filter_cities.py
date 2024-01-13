#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cs = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id"
    cs.execute(query, (sys.argv[4],))
    rows = cs.fetchall()
    city = ', '.join(row[1] for row in rows)
    print(city)

    cs.close()
    db.close()
