#create an write into json file
import json

numbers = [2,3,4,7,11,13]

filename = 'numbers.json'

with open (filename, 'w') as f_obj:
	json.dump(numbers, f_obj)