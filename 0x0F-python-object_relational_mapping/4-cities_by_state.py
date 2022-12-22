#!/usr/bin/python3
""" Script to display all values in the states table
of hbtn_0e_0_usa where name matches argument passed.
Arguments received: mysql username, mysql password,
database name, state name-to-search-for
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    import MySQLdb
    # Open a connection to database and get a cursor
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    # Get the info wanted
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM states INNER JOIN cities \
    WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    results = cursor.fetchall()
    # Print info
    for row in results:
        print(row)
    # Close connection to database and cursor
    cursor.close()
    database.close()
