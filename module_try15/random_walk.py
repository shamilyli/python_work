from random import choice

class RandomWalk():
	"""create a class for random walk"""

	def __init__(self, num_points =5000):
		#initial the # of random step
		self.num_points= num_points
		#initial the x,y to be 0
		self.x_values= [0]
		self.y_values= [0]

	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			#get x_step
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance
			#get y_step
			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance

			#make sure step for x and y are not 0
			if (x_step ==0) and (y_step ==0):
				continue

			#set the next value by value and step
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			#add value to values
			self.x_values.append(next_x)
			self.y_values.append(next_y)