#!/usr/bin/python3

"""The script lists all states with name starting with N"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                 password=argv[2], database=argv[3])
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)
