#!/usr/bin/bash
# The script sends a request to URL and displays the size of the body of the response
curl -sI "$1" | wc -c | xargs | sed 's/$/ /'
