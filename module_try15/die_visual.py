from die import Die
import pygal
#create two die and throw them at the same time
die = Die()
die_0 = Die(10)

results = []
#roll the die for 100 time, then record the reuslt for each time
for roll_num in range(50000):
	result = die.roll() + die_0.roll()
	results.append(result)
print(results)

#analyze the results
frequencies=[]
max_result = die.num_sides + die_0.num_sides
for value in range(2, max_result+1):
	frequency =results.count(value)
	frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('die_visual.svg')

"""
I have done one D6 die histg, two D6 die histg, and D6 + D10 die histg
But the practice only showing D6 + D10
"""