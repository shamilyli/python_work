import csv


filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	print(header_row)

	for index, column_headr in enumerate(header_row):
		print(index, column_headr)

	highs =[]
	for row in reader:
		highs.append(int(row[1]))

	print(highs)

