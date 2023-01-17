#!/bin/bash
# The script displays all HTTP methods that the server accept
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
