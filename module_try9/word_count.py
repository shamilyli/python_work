# counting # of words in multiple files:

def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "sorry, the file " + filename + "does not exist."
		print(msg)
		# if we use ****pass**** instead of print(), there is no ouput for exception.
	else:
		#counting how many words in the txt file
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt','siddhartha.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)