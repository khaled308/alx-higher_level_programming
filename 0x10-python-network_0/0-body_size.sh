#!/bin/bash
# The script displays the size of the body of a URL
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
