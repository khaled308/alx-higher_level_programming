#!/usr/bin/python3
""" Error code #0 """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            """Here the returned response object gives access to all headers"""
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
