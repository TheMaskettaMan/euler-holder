
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

def check_is_prime ( x ) :

	checkme = float(x)
	if ( not checkme.is_integer()) :
		return False
	
	# if divisible by 2, no good.
	if( (checkme / 2).is_integer()) :
		if( checkme == 2 ) :
			return True
		return False
	
	# test odd factors from here on.
	tryodds = 3
	
	primechecked = False
	while( not primechecked ) :
		# append it to the list if our prime factor divides well
		if( (checkme / tryodds).is_integer()) :
			if( checkme == tryodds ) :	
				return True
			else :
				primechecked = True
		# increment our prime by 2 (maintains property of being odd)
		tryodds += 2
	
	return False

