#!/bin/bash
# Sends a GET request to the URL and displays the reponse 
curl -sL -w '%{http_code}' "$1" -o /tmp/output | grep -q '200' && cat/tmp/output
