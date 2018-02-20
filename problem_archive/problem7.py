#!/usr/bin/env python

# Problem 7 10001st prime
# what is the 10001st prime number?

import primehelp

# given 13 is the 6th prime the check begins with discovering 3, the 2nd prime
i = 3
primecount = 1
finalprime = 0


while(primecount < 10001) :
	if ( primehelp.check_is_prime(i)) :
		primecount += 1
		print i
		finalprime = i
	i += 2

print primecount
print finalprime
