filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")# it can do multiple writting
# after this code run, it will create a programming.txt file and write "I love programming." in it.


with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")


"""
model for read: 'r'
model for write: 'w'
model for attach: 'a'
model for read and write: 'r+'

"""