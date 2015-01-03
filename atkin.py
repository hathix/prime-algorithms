#SIEVE OF ATKIN
from math import sqrt
from time import time

LIMIT = 1 * 10 ** 6
sqrtLIMIT = (int)(sqrt(LIMIT)) + 1 # if 1 isn't added, a stray non-prime number sneaks in towards the top of limit because the integer sqrt squared is less than LIMIT

start = time()

# each slot in the primes list represents a number; the slot is true if it's prime but false if it isn't
primes = [False] * LIMIT
# only values of 5+ are sieved in using the algorithm, so manually set 2 and 3
primes[2] = True
primes[3] = True

# put in candidate primes: ints which have odd number of representations by certain quadratic forms
for x in range(1, sqrtLIMIT):
	for y in range(1, sqrtLIMIT):
		n = 4*x*x + y*y
		if n <= LIMIT and (n % 12 == 1 or n % 12 == 5):
			primes[n] = not primes[n]
		n = 3*x*x + y*y
		if n <= LIMIT and (n % 12 == 7):
			primes[n] = not primes[n]
		n = 3*x*x - y*y
		if n <= LIMIT and (n % 12 == 11):
			primes[n] = not primes[n]			
			
# eliminate composites by sieving
for n in range(5, sqrtLIMIT):
	if primes[n]:
		# n is prime, omit multiples of its square
		# this is sufficient because composites which managed to get on the list cannot be square-free
		i = 1
		while(i*n*n < LIMIT):
			primes[i*n*n] = False
			i = i + 1
		
finish = time()
elapsed = finish - start
print("%.3f" % elapsed)
