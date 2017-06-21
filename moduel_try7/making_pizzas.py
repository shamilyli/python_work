import pizza

#module_name.function_name()
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
from module_name import function_name

from module_name import function_0, function_1, function_2

import module_name as mn

form pizza import * #import all function from the module

"""
from pizza import make_pizza as mp

mp(18, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')