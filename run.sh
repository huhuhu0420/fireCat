#!/bin/bash

# ip=$1
# echo $ip

python3 src/app.py &
sleep 0.5
firefox 127.0.0.1:5000/ &
python3 src/connectNcat.py &
sleep 0.3
python3 src/txt2json.py 1.txt 1.json &

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

