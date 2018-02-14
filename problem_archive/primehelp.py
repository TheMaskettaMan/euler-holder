
# finds prime factors of x
# if x isnt an integer return 0
# tryodds tests primes due to the nature of
# the interaction of the outer loop repeatedly factoring lower primes
# out of factorme

def findprimefactors( x ):
	
	factorme = float(x)
	if ( not factorme.is_integer()) :
		return 0
	
	factors = []
	
	# first factor out all instances of 2	
	while( (factorme / 2).is_integer() ) :
		factorme = factorme / 2
		factors.append(2)
	
	print ("finished with 2s")
	
	# second, try all odd factors from this point
	tryodds = 3

	# factorization complete when factorme == 1
	while( factorme > 1 ) :
		# try to divide our prime into factorme,
		# append it to the list if our prime factor divides well
		if( (factorme / tryodds).is_integer() ) :
			factorme = factorme / tryodds
			factors.append( tryodds )
		# increment our prime by 2 (maintains property of being odd)
		else :
			tryodds += 2
	
	return factors


