#!/bin/bash
# The script displays the body of the response from a URL
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
