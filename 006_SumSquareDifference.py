import sys

# Takes the sum of the squares from 1 through n and the square of the sum of 1 through n
# 	Sum of squares is a list sum, generate a list and call the built-in sum function
# 	Square of sums is a mathematical formula
# Takes the absolute value, just in case
def sum_sq_diff(n):
	return abs( sum( x ** 2 for x in range(1, n + 1) ) - ( (n * (n + 1) ) / 2) ** 2 )

if __name__ == '__main__':
	# User inputs n
	print sum_sq_diff( int(sys.argv[1]) )
