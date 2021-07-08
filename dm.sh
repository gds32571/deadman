#!/bin/bash

cd /home/pi/deadman/

let "ctr=0"
while true; do
  echo "$ctr" > "myctr.txt"
  python deadman.py
  echo $? >> "myerr.txt"
  sleep 5
  let "ctr+=1"
done


