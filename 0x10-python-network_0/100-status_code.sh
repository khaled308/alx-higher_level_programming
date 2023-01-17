#!/bin/bash
# The script displays the status of the code of response from a URL
curl -s -o /dev/null -w '%{http_code}' "$1"
