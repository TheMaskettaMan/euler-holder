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

if( (4/2) ) :
	print ("you better see me")

if( factors ) :
	print ("factors?")
	print factors
