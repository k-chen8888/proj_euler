import sys, math

# Product of k numbers in a list, with a defined start time
def prod_from(l, start, k):
	out = 1
	
	for i in range(start, start + k):
		out = out * l[i]
	
	return out

# Finds the maximum product made up of k consecutive elements in the list
def max_prod(l, k):
	max_prod, max_start = 1, 0 
	curr_prod, start = 1, 0
	
	# Continue until taking k elements overshoots the list
	while start + k - 1 < len(l):
		curr_prod = prod_from(l, start, k)
		
		if curr_prod > max_prod:
			max_prod, max_start = curr_prod, start
		
		start = start + 1
	
	return [ max_prod, max_start, l[max_start:max_start + k] ]

# Find the product
if __name__ == '__main__':
	f = open(sys.argv[1], "r")
	number = f.read()
	print max_prod( [ int(i) for i in list(number)[0:1000] ] , int(sys.argv[2]) )
