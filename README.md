#fireCat

## python requirement
* flask
* time 
* pexpect

## self test
1. ncat -l 1234 --chat &nbsp;  //server listen
2. flask --debug run --host=0.0.0.0, open webpage and go to /chat
3. python3 connectNcat.py
4. type sth in the chat box, u can see the content in json file 

## TODO 
* file rename 
* need js to read json data and display on the webpage
* prettier webpage
* bug fix
  * self user code not correct
* switch txt(json) to db
