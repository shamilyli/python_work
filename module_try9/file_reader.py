with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
	print(contents.rstrip())

"""
in linux and os x we use as follow:
with open('text_file/filename.text') as file_object

in windows:
with open('text_file\ filename.txt') as file_object

"""

# reading the file line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)

"""
output:
3.1415926535

8979323846

2643383279

"""

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

"""
# rstrip() method for get rid of bank line:
output:
3.1415926535
8979323846
2643383279
"""