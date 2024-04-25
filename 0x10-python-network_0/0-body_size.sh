#!/bin/bash
# shell script that gets the lenght of an http request sent with curl
curl -s $1 |wc -c
