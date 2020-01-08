#!/bin/bash
# display all HTTP methods the server will accept
curl "$1" -sI | grep Allow | cut -d' ' -f2-4
