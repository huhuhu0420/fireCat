#!/bin/bash

python3 src/app.py &
sleep 0.5
firefox 127.0.0.1:5000/ &

function close () {
  pkill -f "python3 src/app.py"
  echo "close firecat"
  exit
}

trap close SIGINT

while true
do 
  sleep 10
done

