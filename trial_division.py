#TRIAL DIVISION
from math import sqrt
from time import time

LIMIT = 1 * 10 ** 6

start = time()

primes = list()
for a in range(2, LIMIT):
	is_prime = False
	# run this like a function with breakpoints (run once)
	for x in range(0, 1):
		if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
			is_prime = False
			break
		to_test = range(11, (int)(sqrt(a)) + 1)
		for x in to_test:
			if a % x == 0:
				is_prime = False
				break
		is_prime = True
		
	if is_prime:
		primes.append(a)
		
# 2,3,5,7 removed by earlier sieve, put them in here		
primes.insert(0,7)
primes.insert(0,5)
primes.insert(0,3)
primes.insert(0,2)
		
finish = time()
elapsed = finish - start
print("%.3f" % elapsed)