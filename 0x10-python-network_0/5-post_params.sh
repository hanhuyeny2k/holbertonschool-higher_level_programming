#!/bin/bash
# send a POST request to the passed URL and display the body of response
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
