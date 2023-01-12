# python-md5-hash

## A python script to hash all rockyou.txt passwords.

As a Penetration Tester, I had to brute force a web login form, that was converting all of my input to md5. Therefore, I decided to write a quick script that goes through the rockyou.txt file and hashes each line using the md5 algorithm.

Unfortunately, the rockyou.txt file is too large to upload, therefore I am only providing the script.

Usage:

`chmod +x python-md5-hash.py`

`./python-md5-hash.py | tee rockyou-md5.txt`

You can download rockyou.txt from here: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

P.S.: there is surely a better way to do it that is more memory-easy and safe, however this is all I could do :) Hopefully it is useful to someone
