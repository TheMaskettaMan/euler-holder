#!/usr/bin/env python

# Problem 6 Sum of Square difference
# sum of squares of first 10 natural numbers (1^1 + 2^2...) = 385
# the square of the sum of first 10 natural numbers (1+2+3..)^2 = 3025
# hence the difference is 3025 - 385 = 2640
# find the diffference between the sum of squares and square of sum
# of the first 100 natural numbers

squareofsum = 0

sumofsquares = 0

for i in range(101) :
	sumofsquares += i**2
	squareofsum += i

squareofsum = squareofsum**2

print "sum of squares:"
print sumofsquares
print "square of sum:"
print squareofsum

print "difference:"
print (squareofsum - sumofsquares)
