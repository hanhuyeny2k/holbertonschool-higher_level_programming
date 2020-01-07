#!/bin/bash
# Send a request to a URL and display the size of the body of the response
curl "$1" -I -s | grep Content-Length | cut -d' ' -f2
