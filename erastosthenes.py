#SIEVE OF ERASTOSTHENES
from math import sqrt
from time import time

LIMIT = 1 * 10 ** 6
sqrtLIMIT = (int)(sqrt(LIMIT)) + 1 # if 1 isn't added, a stray non-prime number sneaks in towards the top of limit because the integer sqrt squared is less than LIMIT

start = time()

# each slot in the primes list represents a number; the slot is true if it's prime but false if it isn't
primes = [True] * LIMIT

# sieve out anything that's a multiple of 2, 3, 5, ... 
for i in range(2, sqrtLIMIT):
	if primes[i]:
		j = 2
		while j*i < LIMIT:
			primes[j*i] = False
			j = j + 1
		
finish = time()
elapsed = finish - start
print("%.3f" % elapsed)