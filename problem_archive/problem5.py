#! /bin/usr/env python

# Problem 5
# 2520 is the lowest number cleanly divisible by 1-10
# what is the lowest number cleanly divisible by 1-20?


# Check a given number to see if it is divisible by a certain range
# if desired I could make the range of divisors checked a parameter
def check_clean_division ( checkme ) :
	check = float(checkme)
	for x in range(1,21) :
		if( not (check / x).is_integer() ) :
			return False
	return True


found = False
divisible = 0
# start at 20 and increment by 20 since our number requires a largest divisor of 20
# TODO: modify entire program to bypass hard coding of 20

largest_divisor = 20
i = 20
while (not found) :
	if(check_clean_division(i)) :
		print i
		found = True
	i += largest_divisor






