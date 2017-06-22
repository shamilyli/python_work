# open a json file and read data inside of the file

import json

filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")

