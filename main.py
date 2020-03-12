# Author: 107000270
# Date	: 12 Mar, 2020

import csv

# Reading csv file
cwb_filename = '107000270.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
	mycsv = csv.DictReader(csvfile)
	header = mycsv.fieldnames
	for row in mycsv:
		data.append(row)

# Function for extracting data of interest
def myFilter(item):
	if((item['station_id'] == 'C0A880' or \
		item['station_id'] == 'C0F9A0' or \
		item['station_id'] == 'C0G640' or \
		item['station_id'] == 'C0R190' or \
		item['station_id'] == 'C0X260') and \
		item['TEMP'] != '-99.000' and \
		item['TEMP'] != '-999.000'):

		return True
	else:
		return False

# Extract data of interest
target_data = list(filter(myFilter, data))

# Find maximum temperature
maxval = [-999, -999, -999, -999, -999]
for dp in target_data:
	if dp['station_id'] == 'C0A880' and float(dp['TEMP']) > maxval[0]:
		maxval[0] = float(dp['TEMP'])
	if dp['station_id'] == 'C0F9A0' and float(dp['TEMP']) > maxval[1]:
		maxval[1] = float(dp['TEMP'])
	if dp['station_id'] == 'C0G640' and float(dp['TEMP']) > maxval[2]:
		maxval[2] = float(dp['TEMP'])
	if dp['station_id'] == 'C0R190' and float(dp['TEMP']) > maxval[3]:
		maxval[3] = float(dp['TEMP'])
	if dp['station_id'] == 'C0X260' and float(dp['TEMP']) > maxval[4]:
		maxval[4] = float(dp['TEMP'])

for i in range(5):
	if maxval[i] == -999:
		maxval[i] = 'None'

# Print result
result = [['C0A880', maxval[0]], ['C0F9A0', maxval[1]], ['C0G640', maxval[2]], ['C0R190', maxval[3]], ['C0X260', maxval[4]]]

print(result)