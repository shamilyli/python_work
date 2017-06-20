#if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())
#check  bmw in list of cars

banned_users = ['andrew', 'carolina', 'david']
user ='marie'

if user not in banned_users:
	print(user.title())
#check marie in banned_users

age = 12
if age <4:
	print("your addmission cost is 0")
elif age <18:
	print("your addmission cost is 5")
else:
	print("your addmission cost is 10")
# test for if-elif-else statement