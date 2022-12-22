#!/usr/bin/python3
"""
Script to list all states from database hbtn_0e_0_usa.
Arguments are as follows: mysql username, mysql password, database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Getting data from hbtn_0e_0_usa"""
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    INNER JOIN states ON states.id = cities.state_id \
    WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC", (argv[4], ))
    list_of_states = cursor.fetchall()
    """Print results"""
    for s, states in enumerate(list_of_states):
        if s != 0:
            print(", {:s}".format(states[0]), end='')
        else:
            print("{:s}".format(states[0]), end='')
    print()
    """Close cursor and connection to database"""
    cursor.close()
    database.close()
