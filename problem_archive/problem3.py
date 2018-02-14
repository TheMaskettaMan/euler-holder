#!/usr/bin/python

#problem 3 find the largest prime
#factor of 600851475143

import primehelp

primefactors = primehelp.findprimefactors(600851475143)

print primefactors

max = 0
for i in primefactors :
	if( i > max) :
		max = i
	print i	
print "max"
print max
