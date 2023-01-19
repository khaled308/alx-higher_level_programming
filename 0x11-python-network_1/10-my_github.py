#!/usr/bin/python3
""" Github credentials """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]

    try:
        r = requests.get(url, auth=(username, password)).json()
        print(r["id"])
    except:
        print("None")
