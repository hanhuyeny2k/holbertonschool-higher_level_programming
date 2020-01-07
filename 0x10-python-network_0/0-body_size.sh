#!/bin/bash
# Takes in a URL, sends a request to that URL and displays the size of the body
# of the response
curl "$1" -I -s | grep -Fi Content-Length | cut -d ' ' -f2
