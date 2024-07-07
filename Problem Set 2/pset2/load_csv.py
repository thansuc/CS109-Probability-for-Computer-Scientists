# pylint: disable = mixed-indentation
'''
A useful library for reading files
with "comma seperated values", or csv.

File: Load CSV Example
----------------------
This is some sample code. Use it in any way
that you would like. It is meant to both give
you a head start on the assignments and show you
what some python code looks like :-)
- Written by Chris Piech fall 2018, edited by Tim Gianitsos fall 2019
'''

import csv

def main():
	'''The main method'''
	data = load_csv_data('prior.csv')
	print_data(data)

def load_csv_data(file_name):
	'''
	Reads a file into a 2d array. There are
	other ways of doing this (check out numpy).
	But this shows one such way.
	'''
	matrix = []
	# open a file
	with open(file_name) as file:
		reader = csv.reader(file)

		# loop over each row in the file
		for row in reader:

			# cast each value to a float
			double_row = []
			for value in row:
				double_row.append(float(value))

			# store the row into our matrix
			matrix.append(double_row)
	return matrix

def print_data(matrix):
	'''Prints out a 2d array'''
	for row in matrix:
		print(row)

# The condition is True only if this file is run as a script
# (e.g. python3 <this file>.py). It will be False if this
# file is used in an import statement
if __name__ == '__main__':
	main()
