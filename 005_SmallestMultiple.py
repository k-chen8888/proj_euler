import sys, operator, math

# Naive way to check if a number is a prime
def is_prime(n):
	return True if all( n % i != 0 for i in range( 2, int( math.sqrt(n) + 1 ) ) ) else False

# Gets all prime factors with repeats for each number up to n
def prime_factorize_all(n):
	p = []
	
	for i in range(1, n):
		p.append( prime_factorization(i) )
	
	return p

# Gets the prime factorization for some number n
def prime_factorization(n):
	p = []
	
	# Start at 2
	i = 2
	
	# Factorization
	while i <= n:
		temp = n
		
		# Repeat factors
		while (temp % i) == 0 and is_prime(i):
			p.append(i)
			temp /= i
		
		# Test next odd number
		i = i + 1 if i == 2 else i + 2
	
	return p

# Takes a list of factors of numbers and a number to test
# Returns a pair (number, maximum repeats within a factor list)
def count_repeats(all_factors, n):
	max_count = 0
	
	for factor_list in all_factors:
		max_count = factor_list.count(n) if factor_list.count(n) > max_count else max_count
	
	return [n, max_count]

# Takes a list of [number, count] pairs
# Find the product of all number ** count
def repeat_prod(repeat):
	prod = 1
	
	for i in repeat:
		prod *= i[0] ** i[1]
	
	return prod

if __name__ == '__main__':
	factors = prime_factorize_all( int( sys.argv[1] ) + 1 )
	print factors
	
	repeats = [ count_repeats(factors, i) for i in range(1, len(factors) + 1) ]
	
	print repeat_prod(repeats)
