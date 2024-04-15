#!/usr/bin/python3
"""A module that reads the state in a db using user input"""

import sys
import MySQLdb


def connection(username, password, db_name, searched_name):
    """The function that connects to the db"""

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")

    curr = conn.cursor()

    query = """SELECT * FROM cities LEFT JOIN states ON cities.state_id = states.id  WHERE BINARY cities.name=%s
"""

    curr.execute(query, (searched_name,))

    query_rows = curr.fetchall()

    for rows in query_rows:
        print(rows)

    curr.close()
    conn.close()


if __name__ == '__main__':
    connection(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
