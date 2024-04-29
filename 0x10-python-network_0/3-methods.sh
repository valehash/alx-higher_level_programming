#!/bin/bash
#script to find the allowed methods on a server wtih the ip addres
curl -sI $1| grep "Allow" |awk '{$1=""; print $0}'
