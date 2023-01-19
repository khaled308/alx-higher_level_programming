#!/usr/bin/python3
"""The script displays the body of the response from an email to the URL"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    infor = urlencode({'email': argv[2]}).encode('ascii')
    request = Request(argv[1], infor)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
