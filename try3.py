magicians = ["amy", "lucy", "jimmy"]
for magician in magicians:
	print(magician)
""" 
output: 
amy
lucy
jimmy 
"""
#Regular Errors:
#IndentationError: expected an indented block
#IndentationError: unexpected indent
#SyntaxError: invalid syntax

for value in range(1,5):
	print(value)
# output : 1,2,3,4
# if we want the output is 1,2,3,4,5
# then we need rang(1,6) instead

#creating a list of #
numbers = list(range(1,6))
print(numbers)#[1, 2, 3, 4, 5]

even_numbers = list(range(2,11,2))
print(even_numbers) #[2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square) #squares.append(value**2)
print(squares)
#simple form
squares = [value**2 for value in range(1,11)]
print(squares)

"""
output:
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))#min number
print(max(digits))#max number
print(sum(digits))#sum of all numbers in digits

squares = [value**2 for value in range(1,11)]
print(squares)

#copy list
my_foods =['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[1:]
print(my_foods)
print(friend_foods)


dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
for dimension in dimensions:
	print(dimension)
# we can't change Tuple
