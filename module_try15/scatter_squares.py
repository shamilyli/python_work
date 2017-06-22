import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#camp for the changing color
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
#title
plt.title("Square Number", fontsize=24)
#x label
plt.xlabel("Value ", fontsize =14)
#y label
plt.ylabel("Square of Value", fontsize=14)
#number in x,y axis
plt.tick_params(axis='both', which = 'major', labelsize=10)
#setting the range for axis
plt.axis([0,1100,0,1100000])

#save the image to squares_plot.png
plt.savefig('squares_plot.png', bbox_inches='tight')