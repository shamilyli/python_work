import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_values= [1,2,3,4,5]

#width of line
plt.plot(input_values, squares, linewidth =5)
#title
plt.title("Square Number", fontsize=24)
#x label
plt.xlabel("Value ", fontsize =14)
#y label
plt.ylabel("Square of Value", fontsize=14)
#number in x,y axis
plt.tick_params(axis='both', labelsize=10)
plt.show()