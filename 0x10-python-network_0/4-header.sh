#!/bin/bash
# URL as an argument,sends GET request to the URL with a header variable, and displays body of the response
curl -sH "X-School-User-Id: 98" "$1"
