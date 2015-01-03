#EFFICIENCY
from math import sqrt
from time import time

LIMIT = 1 * 10 ** 6

start = time()

sqrtlim=sqrt(float(LIMIT))
pp=2
ep=[pp]
ss=[pp]
pp+=1
i=0
rss=[ss[0]]
tp=[pp]
xp=[]
pp+=ss[0]
npp=pp
tp.append(npp)
rss.append(rss[i]*tp[0])
while npp<int(LIMIT):
		i+=1
		while npp<rss[i]+1:
				for n in ss:
						npp=pp+n
						if npp>int(LIMIT): break
						if npp<=rss[i]+1: pp=npp
						sqrtnpp=sqrt(npp)
						test=True
						for q in tp:
								if sqrtnpp<q: break
								elif npp%q==0:
										test=False
										break
						if test:
								if npp<=sqrtlim: tp.append(npp)
								else: xp.append(npp)
				if npp>int(LIMIT): break
		if npp>int(LIMIT): break
		lrpp=pp
		nss=[]
		while pp<(rss[i]+1)*2-1:
				for n in ss:
						npp=pp+n
						if npp>int(LIMIT): break
						sqrtnpp=sqrt(npp)
						test=True
						for q in tp:
								if sqrtnpp<q: break
								elif npp%q==0:
										test=False
										break
						if test:
								if npp<=sqrtlim: tp.append(npp)
								else: xp.append(npp)
						if npp%tp[0]!=0:
								nss.append(npp-lrpp)
								lrpp=npp
						pp=npp
				if npp>int(LIMIT): break
		if npp>int(LIMIT): break
		ss=nss
		ep.append(tp[0])
		del tp[0]
		rss.append(rss[i]*tp[0])
		npp=lrpp
i=nss=npp=n=sqrtnpp=test=q=r=lrpp=rss=ss=pp=sqrtlim=0
ep.reverse()
[tp.insert(0,a) for a in ep]
tp.reverse()
[xp.insert(0,a) for a in tp]

finish = time()
elapsed = finish - start
print("%.3f" % elapsed)