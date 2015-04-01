import sys, operator, math

# Gets factors
def factorize(n):
	return list( reduce( operator.add, [ (x, n/x) for x in range(1, int(math.sqrt(n) + 1)) if (n % x == 0) ], () ) )

# Determines if a number is prime
def is_prime(n):
	return True if len(factorize(n)) == 2 else False

# Product of all numbers in a list
def set_product(some_set):
	return reduce( lambda x, y: x * y, some_set )

if __name__ == '__main__':
	factors = [ factorize(x) for x in range( 1, int( sys.argv[1] ) + 1 ) ]
	factor_list = []

	# Clean up list
	for i in range(0, len(factors)):
		
		# Add numbers iff they are prime
		[factor_list.append(x) for x in factors[i] if is_prime(x)]
	
	print set(factor_list)
	
	prod = set_product( list( set(factor_list) ) )
	
	# Certain numbers need to be duplicated
	# To be exact, the squares need to be put in again
	for i in range(1, int( sys.argv[1] ) + 1 ):
		if i ** 2 < int( sys.argv[1] ) + 1:
			prod = prod * i
	
	print prod
