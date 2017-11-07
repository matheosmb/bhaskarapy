import math;

class bhaskara():
	a = int(input("Type the first coefficient"));
	b = int(input("Type the second coefficent"));
	c = int(input("Type the third coefficient"));

	def calculation(self):
		delta = (self.b**2-4*self.a*self.c);
		print(delta)

		if(delta < 0):
			print ("This algorithm does not support imaginary roots")
			variables = self.entry()	#One more time, we call the function entry and store to variables again.
			delta = (variables[1]**2 - 4*variables[0]*variables[2])

		elif (delta > 0):
			x1 = (-self.b+math.sqrt(delta))/(2*self.a);
			x2 = (-self.b-math.sqrt(delta))/(2*self.a);
			print ("The first root is: {}" .format(x1));
			print ("The second root is: {}" .format(x2));

		else:
			x1 = (-self.b+math.sqrt(delta))/(2*self.a);
			print("The only root is: {}" .format(x1));
			
b = bhaskara();
b.calculation();
