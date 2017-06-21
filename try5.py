# how to use dictionary
alien_0 = {'color':'green', 'point':5}
print(alien_0['color'])# green
print(alien_0['point'])# 5

print(alien_0)#{'color': 'green', 'point': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)#{'color': 'green', 'y_position': 25, 'x_position': 0, 'point': 5}


alien_0['x_position']= alien_0['x_position']+1 # modifiy x_position
print(alien_0)#{'color': 'green', 'y_position': 25, 'x_position': 1, 'point': 5}

del alien_0['point']# delete point from the dictionary
print(alien_0)#{'color': 'green', 'y_position': 25, 'x_position': 1}

for key, value in alien_0.items():
	print("\nkey: " + key)
	print("value:" + str(value))
"""
output:
key: color
value:green

key: y_position
value:25

key: x_position
value:1
"""

favorite_languages = { 'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python', }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " +name.title() +
			", I see your favorite language is "+
			favorite_languages[name].title() + " !")


for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

for language in set(favorite_languages.values()):
	print(language.title()) # set() the element can't repeat


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'], 
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
"""
output
Sarah's favorite languages are:
	C

Edward's favorite languages are:
	Ruby
	Go

Jen's favorite languages are:
	Python
	Ruby

Phil's favorite languages are:
	Python
	Haskell
"""

#practices for many users
users = { 
'aeinstein': {
'first': 'albert', 
'last': 'einstein', 
'location': 'princeton',
'favorite_languages':['python', 'ruby'] },
'mcurie': {
'first': 'marie', 'last': 'curie', 'location': 'paris','favorite_languages':['c'] },
}

for username, user_info in users.items():
	print("\nUsername:" + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	languages = user_info['favorite_languages']

	print("\tFull name: " + full_name.title()) 
	print("\tLocation: " + location.title())
	print("\tlanguages: ")
	for language in languages:
		print("\t\t" + language.title())
"""
output:
Username:aeinstein
	Full name: Albert Einstein
	Location: Princeton
	languages: 
		Python
		Ruby

Username:mcurie
	Full name: Marie Curie
	Location: Paris
	languages: 
		C
"""
