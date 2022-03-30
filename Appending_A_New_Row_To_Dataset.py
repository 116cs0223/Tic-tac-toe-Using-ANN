# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:49:33 2022

@author: SUBHAM SAHOO
"""

# Import writer class from csv module
from csv import writer

# List
new_row= [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0] + [0, 0, 0, 1, 0, 0, 0, 0, 0]

# Open our existing CSV file in append mode
# Create a file object for this file
with open('dataset.csv', 'a', newline='') as f_object:

	# Pass this file object to csv.writer()
	# and get a writer object
	writer_object = writer(f_object)

	# Pass the list as an argument into
	# the writerow()
	writer_object.writerow(new_row)

	#Close the file object
	f_object.close()
