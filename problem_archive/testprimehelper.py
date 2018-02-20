#!/usr/bin/env python

# helps test prime functions.
# Will eventually be updated to a better example of "unit tests"
import primehelp

print ("hey man")

factors = primehelp.findprimefactors(14)

if( (float(5)/2).is_integer() ) :
	print ("what the fuck")

if( primehelp.findprimefactors(2.5)) :
	print ("oh no you dont see me")
if( primehelp.findprimefactors(7) ) :
	print "its prime but can you see me?"
	print primehelp.findprimefactors(7)

print "checkprime tests"

if (primehelp.check_prime(7)) :
	print "you should see me"
if (primehelp.check_prime(4)) :
	print "you shouldnt see me"

if (primehelp.check_prime(9)) :
	print "you shouldnt see me"

if( factors ) :
	print ("factors?")
	print factors
