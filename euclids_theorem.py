

# Python program to demonstrate working of extended
# Euclidean Algorithm
	

# Function to return gcd of a and b
def gcd(a, b):
	if a == 0 :
		return b
	
	return gcd(b%a, a)

# function for extended Euclidean Algorithm
def gcdExtended(a, b):

	# Base Case
	if a == 0 :
		return b, 0, 1
			
	gcd, x1, y1 = gcdExtended(b%a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd, x, y
	

# Driver code
a, b = 3500,1525
g, x, y = gcdExtended(a, b)
print("gcd(", a , "," , b, ") = ", g)