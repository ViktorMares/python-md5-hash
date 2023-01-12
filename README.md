# python-md5-hash

## A python script to hash all rockyou.txt passwords.

As a Penetration Tester, I had to brute force a web login form, that was converting all of my input to md5. Therefore, I decided to write a quick script that goes through the rockyou.txt file and hash each line using the md5 algorithm.

Usage:

`chmod +x python-md5-hash.py`

`./python-md5-hash.py | tee rockyou-md5.txt`

You can download rockyou.txt from here: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
