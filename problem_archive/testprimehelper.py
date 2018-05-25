#!/usr/bin/env python

# helps test prime functions.
# Will eventually be updated to a better example of "unit tests"
# also serves as a python training ground
import primehelp

factors = primehelp.findprimefactors(14)


if( (float(5)/2).is_integer() ) :
	print ("should be failing")

if( primehelp.findprimefactors(2.5)) :
	print ("shouldnt see me")

if( primehelp.findprimefactors(7) ) :
	print "should be visible"
	print primehelp.findprimefactors(7)

print "checkprime tests"

if (primehelp.check_prime(7)) :
	print "you should see me"

if (primehelp.check_prime(4)) :
	print "you shouldnt see me"

if (primehelp.check_prime(9)) :
	print "you shouldnt see me"

if( factors ) :
	print ("factors:")
	print factors
