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

#define a function print_models and show_completed_models
#each function have a unique job
def print_models (unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		print("printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nthe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecaherdon']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


#pass any paremeter in making a pizza example
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size)+"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " +topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#user_profile.py
#**user_info can have more thant one paremeters input, as long as they have more key, value
def build_profile(first, last, **user_info):
	profile ={}
	profile['first_name']= first
	profile['last_name']= last
	for key, value in user_info.items():
		profile[key]= value
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)




