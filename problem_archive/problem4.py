

#Problem 4, the largest palindrome created by multiplying two 2 digit numbers is
# blah blah blah

# find the largest palindrome created by multiplying two 3 digit numbers

def is_palindrome( check ) :
	
	tocheck = str(check)
	length = len(tocheck)

	for i in range(length / 2) :
		if( not tocheck[i] == tocheck[length - (i + 1) ] ) :
			return False
	
	return True
	

largest_palindrome = 0
largest_components = [0,0]


for x in range(99,1000) :
	
	for y in range(99,1000) :

		product = x * y
		if( is_palindrome( product ) and product > largest_palindrome ) :
			largest_palindrome = product
			largest_components = [x,y]


print "largest palindrome"
print largest_palindrome
print largest_components
