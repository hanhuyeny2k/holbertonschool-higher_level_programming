#!/bin/bash
# send a GET request to the URL and display the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
