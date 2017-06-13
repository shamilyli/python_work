#1.hello world
print("Hello Python world!")


#2.2.11 nameing variable & using variable
message = "Hello Python world!"
print(message)


message = "Hello Python Crash Course world!"
print(message)


# 2.2.2 use variable and avoid nameing mistake

message = "Hello Python Crash Course reader!"
# print(mesage) # typing mistake
# 'to test it we can comment out the typing mistake'

# 2.3 character string
# **single quote can allow ",", and """ inside of character string**
character_string_one = "This is a string."

character_string_two = 'This is also a string.'

character_string_three =  'I told my friend, "Python is my favorite language!"'

character_string_four = "The language 'Python' is named after Monty Python, not the snake."

character_string_five = "One of Python's strengths is its diverse and supportive community."

print(character_string_one)
print(character_string_two)
print(character_string_three)
print(character_string_four)
print(character_string_five)


#2.3.1 text transform
name = "ada lovelace"
name_one = 'jimmy huang'
print(name.title())
print(name_one.title())

#upper case, lower case
print(name.upper())
print(name.lower())

# joint character string
fist_name ="jimmy"
last_name = "huang"
full_name = fist_name + " " +last_name + "!"
print(full_name)

message = "Hello, " +full_name.title()
print(message)

#2.3.3 use tab and newline
#\t and \n
print("\tpython")

print("languages:\n\tPython\n\tJavaScript\t\nJava")

# 2.3.4 delete the blank
favorite_language = '  python'
print(favorite_language)
favorite_language= favorite_language.rstrip()
print(favorite_language)
