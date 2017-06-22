#deal with ZeroDivisionError exception:
"""
print(5/0)
...output...
Traceback (most recent call last):
  File "division.py", line 3, in <module>
    print(5/0)
ZeroDivisionError: division by zero
"""

try:
	print(5/0)
except ZeroDivisionError:
	print("you can't divide by zero!")



#practice
print("give me two numbers, and i will divide them.")
print("enter 'q' to quit")

while True:
	first_number = input("\n First number: ")
	if first_number =='q':
		break
	second_number = input("\n Second number: ")
	if second_number =='q':
		break
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("you can't divide by zero!")
	else:
		print(answer)