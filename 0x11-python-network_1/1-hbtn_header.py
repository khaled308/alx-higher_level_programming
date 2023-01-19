#!/usr/bin/python3
"""The script displays the value of X-Request-Id from a URL"""

from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    request = Request(argv[1])
    with urlopen(request) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
