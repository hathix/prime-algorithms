Prime Number Algorithms
================

Various Python algorithms to find and list prime numbers.

Included:

* [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin) (a fast, modern optimization of the Sieve of Erastosthenes)
* Efficiency, a custom script
* [Sieve of Erastosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) (the famous one)
* [Trial Division](https://en.wikipedia.org/wiki/Trial_division), a very naive approach
* [Sieve of Zakiya](https://www.scribd.com/doc/73385696/The-Sieve-of-Zakiya) (a super-optimized algorithm created by a Yahoo programmer)

### Rationale

Created for the Pennsylvania Junior Academy of Science, 2013. For this project I implemented the above algorithms to find every prime number up to a certain limit and tested their runtimes.

### When to use

Use these algorithms when you need to **find a long list of prime numbers**, or if you just need to **find a large prime number**. These algorithms were tested with numbers up to 10^7.

### Data

I normalized each algorithm's average runtime to assign it a 'score'; faster algorithms have lower scores.

| Algorithm | Score (lower is faster) |
|-----------|-------------------------|
| Sieve of Zakiya | 2.244 |
| Sieve of Erastosthenes | 13.504 |
| Sieve of Atkin | 19.386 |
| Efficiency | 66.263 |
| Trial Division | 398.603 |

### Conclusions:

* **Basically, use the Sieve of Zakiya.** It's not too hard to translate to other programming languages.
* The Sieve of Atkin is supposed to be an optimized version of the Sieve of Erastosthenes, but it's actually slower.
* Don't roll your own prime number finding algorithm.
* And please please please don't use trial division, where you divide every number *n* by every number from 1 to *n/2* inclusive.
