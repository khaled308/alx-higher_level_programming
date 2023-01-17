#!/bin/bash
# The script displays the body of the response of a URL
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d ' ' -f2)" = '200' ]; then curl -sL "$1"; fi
