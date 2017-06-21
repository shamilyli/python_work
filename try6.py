# Review for input() and while loop
message = raw_input("Tell me something, and I will repeat it back to you: ")
print(message)

name = raw_input("Please enter your name: ")
print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = raw_input(prompt)
print("\nHello, " + name + "!")

age = raw_input("how old are you?")
age = int(age)
print(age>=18)

"""
for python 2.7 we use raw_input() instead of input()
"""
