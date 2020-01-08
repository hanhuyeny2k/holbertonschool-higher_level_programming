#!/bin/bash
# send a delete request to the URL passed as the first arg and display the body
curl -sX "DELETE" "$1"
