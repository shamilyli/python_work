# deal with FileNotFoundError
"""
filename ='alice.txt'

with open(filename) as f_obj:
	contents = f_obj.read()
Traceback (most recent call last):
  File "alice.py", line 4, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""

filename ='alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "sorry, the file " + filename + "does not exist."
	print(msg)
else:
	#counting how many words in the txt file
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")

