#!/bin/bash

python3 src/app.py &
sleep 0.5
firefox 127.0.0.1:5000/ &
python3 src/connectNcat.py &

function close () {
  pkill python3
  echo "close"
  exit
}

trap close SIGINT

while true
do 
  sleep 10
done

