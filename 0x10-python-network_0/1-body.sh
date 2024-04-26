#!/bin/bash
#code to get the body if a webpage if the header response is 200
[ $(curl -o /dev/null -s -w "%{http_code}" $1 ) -eq 200 ] && curl -sI $1
