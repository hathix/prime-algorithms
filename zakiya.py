#SIEVE OF ZAKIYA
from math import sqrt, ceil
from time import time

LIMIT = 1 * 10 ** 6

start = time()

# all prime candidates > 5 are of form 30*k+(1,7,11,13,17,19,23,29)
residues = [1,7,11,13,17,19,23,29,31]   

num = LIMIT-1 | 1            # if LIMIT even number then subtract 1
mod=30; rescnt=8             # modulus value; number of residues
k=num/mod; modk = mod*k; r=1 # kth residue group, base num value
while num >= modk+residues[r]: r +=1  # find last pc position <= num
maxprms = k*rescnt + r-1     # max number of prime candidates
prms = [True]*maxprms        # set all prime candidates to True

# hash of residues offsets to compute nonprimes positions in prms
pos = {}
for i in xrange(rescnt): pos[residues[i]] = i-1

# sieve to eliminate nonprimes from prms
sqrtN = int(ceil(sqrt(num)))
modk=r=0
for prm in prms:
	r += 1
	if r > rescnt: r = 1; modk += mod
	if not prm: continue
	prime = modk + residues[r]
	if prime > sqrtN: break
	prmstep = prime*rescnt
	for ri in residues[1:]:
		product = prime*(modk+ri)
		# compute product position index in prms
		k,rr = divmod(product,mod)
		nonprmpos = k*rescnt + pos[rr]
		for nprm in xrange(nonprmpos,maxprms,prmstep): prms[nprm] = False

# the prms array now has all the positions for primes 7..N
primes = [2,3,5]
modk=r=0
for prime in prms:
	r += 1
	if r > rescnt: r = 1; modk += mod
	if prime: primes.append(modk+residues[r])

finish = time()
elapsed = finish - start
print("%.3f" % elapsed)