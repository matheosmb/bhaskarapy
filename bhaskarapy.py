def entry():
	a = input ("Type the first coefficient")
	b = input ("Type the second coefficent")
	c = input ("Type the third coefficient")
	return a,b,c

def calculation ():
	#Since we are going to use sqrt, to make things easier we import the math library before
	from math import sqrt
	variables = entry()	#We are receiving the parameters from entry function and storing to variables
	delta = (variables[1]**2 - 4*variables[0]*variables[2])

	while (delta  < 0): 
		print ("This algorithm does not support imaginary roots")
		variables = entry()	#One more time, we call the function entry and store to variables again.
		delta = (variables[1]**2 - 4*variables[0]*variables[2])

	if (delta >= 0):
		x1 = (-variables[1] + sqrt(delta))/(2*variables[0])
		x2 = (-variables[1] - sqrt(delta))/(2*variables[0])
		print ("The first root is: "), x1
		print ("The second root is: "), x2
calculation() 		
