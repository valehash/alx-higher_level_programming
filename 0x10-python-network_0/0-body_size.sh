#!/usr/bin/env bash
# shell script that gets the lenght of an http request sent with curl
url=$1
curl -s $url |wc -c
