import json

# checking if the username.json file exist or not
# if the file exist, then print welcome
# otherwise, ask the name of the user
# store the username in json file
# and giving out a print out respond
def greet_user_old():
	filename = 'username.json'

	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("what is your name?")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

# refactor the code:


def greet_user():
	username = get_stored_username()
	if username:
		print("welcome back, " +username + " !")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")


def get_new_username():
	username = input("what is your name?")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

greet_user()