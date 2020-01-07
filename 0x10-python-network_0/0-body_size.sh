#!/bin/bash
# Takes the URL isplays the size of the body of the response
curl "$1" -I -s | grep Content-Length | cut -d' ' -f2
