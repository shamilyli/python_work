# function in python

#define a function and pass paremeter
def greet_user(username):
	print("hallo, " +username.title()+ "!")

greet_user('jimmy')
greet_user('tommy')

def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimmy','huang')
print(musician)


def build_person(first_name, last_name, age=''):
	person = {'first' : first_name, 'last': last_name}
	if age:
		person['age'] =age
	return person

musician = build_person('jimi', 'hendrix',age =27)
print(musician)

while True:
	print("\n please tell me your name:")
	f_name = raw_input("first name:")
	if f_name == 'q':
		break
	l_name = raw_input("last name:")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")

#paremeter for list
def greet_users(names):
	for name in names:
		msg = "hello, " + name.title() + "!"
		print(msg)

usernames = ['jimmy','jim','amy']
greet_users(usernames)