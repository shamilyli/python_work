#30 digits pi
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string=''

for line in lines:
	#pi_string +=line.rstrip()
	#in order to get rid of the space, we are going to use strip() method instead
	pi_string +=line.strip()

print(pi_string)
print(pi_string[:52] + "...") # we only ask to print the first 52 number

print(len(pi_string))


#1,000,000 digits pi
filename ='pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string=''

for line in lines:
	pi_string +=line.strip()

print(pi_string[:52] + "...") # we only ask to print the first 52 number

print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")