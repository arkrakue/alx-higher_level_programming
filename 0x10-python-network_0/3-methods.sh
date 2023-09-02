#!/bin/bash
#Script takes URL ans displays all the HTTP method the server will accept
curl -sI -X OPTIONS "$1" | grep -i Allow | awk -F ': ' '{print $2}'
