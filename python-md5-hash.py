#!/usr/bin/env python3

import hashlib

# Initialize an empty list that we will use to append all the passwords from our file
empty_list = []


# Open the desired file (rockyou.txt in our case) and use the latin 1 encoding to avoid byte errors
with open('rockyou.txt', 'r', encoding='latin-1') as rockyou:
	for pw in rockyou:
		if pw != '':
			empty_list.append(str(pw.strip()))


# Go through each password and hash it using the MD5 algorithm
for password in empty_list:
	print(hashlib.md5(f'{password}'.encode()).hexdigest())
