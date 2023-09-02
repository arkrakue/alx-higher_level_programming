#!/bin/bash
# Delete the URL request passed as the first argument and delete the response
curl -s -X DELETE "$1"
