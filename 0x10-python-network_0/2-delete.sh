#!/bin/bash
#code to get the body if a webpage if the header response 0is 200
curl -X DELETE /dev/null -s -w "%{http_code}" $1 | cat 
