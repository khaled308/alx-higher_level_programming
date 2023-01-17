#!/bin/bash
# The script displays the body of the response after deleting a request to a URL
curl -s "$1" -X DELETE
