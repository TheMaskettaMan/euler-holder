#!/usr/bin/python

#problem2 add even numbers in fibonacci sequence
# less than 4000000

sum = 0
i = 0

# placeholders for fibonacci sequence
a = 1
b = 1
c = 0

finished = False

while(not finished):
	c = a + b;
	if(c > 4000000):
		finished = True
		break

	#with i = 0 and a and b starting our sequence
	#with c==2, every third number number afterwards
	#will be even	
	if(i % 3 == 0):
		sum += c
	
	a = b
	b = c
	i += 1

print(sum)
