# while loop
current_number= 1
while current_number <=5:
	print(current_number)
	current_number +=1
"""
output
1,2,3,4,5
"""


#practice for while loop and raw_input()
prompt = "\nTell me something, and I will repeat it back to you:(p1)"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message !='quit':
	message = raw_input(prompt)

	if message !='quit':
		print(message)

#practice use flag
prompt = "\nTell me something, and I will repeat it back to you:(p2)"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = raw_input(prompt)

	if message =='quit':
		active= False
	else:
		print(message)
#practice use break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = raw_input(prompt)

	if city =='quit':
		break# go out from while loop
	else:
		print("I'd love to go to " + city.title() +"!")

#practice use continue
current_number = 0
while  current_number <10:
	current_number +=1
	if current_number%2 ==0:
		continue# go back to the while loop
	print(current_number)

#avoid end up to infinite loop

#confirmed_users.py
unconfirmed_users = ['alice', 'brain','candace']
confirmed_users=[]

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " +current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print("\t"+confirmed_user.title())

#remove() 'cat' from the list
pets= ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

#fill in the dictionary
responses = {}

polling_active =True

while polling_active:
	name = raw_input("\nwhat is your name?")
	response = raw_input("which mountain would you like to climb someday?")

	responses[name] = response

	repeat =raw_input("would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n--- poll results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
