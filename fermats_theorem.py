def __gcd(a,b):

	if(b == 0):
		return a
	else:
		return __gcd(b, a % b)
	
# To compute x^y under modulo m
def power(x,y,m):

	if (y == 0):
		return 1
	p = power(x, y // 2, m) % m
	p = (p * p) % m

	return p if(y % 2 == 0) else (x * p) % m

# Function to find modular
# inverse of a under modulo m
# Assumption: m is prime
def modInverse(a,m):

	if (__gcd(a, m) != 1):
		print("Inverse doesn't exist")

	else:

		# If a and m are relatively prime, then
		# modulo inverse is a^(m-2) mode m
		print("Modular multiplicative inverse is ",
			power(a, m - 2, m))


def fermat_last_theorem(limit, n) :
 
    if (n < 3):
        return
     
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
         
            # Check if there exists a triplet
            # such that a^n + b^n = c^n
            pow_sum = pow(a, n) + pow(b, n)
            c = pow(pow_sum, 1.0 / n)
            c_pow = pow(int(c), n)
             
            if (c_pow == pow_sum):
                print("Count example found")
                return
    print("No counter example within given range and data")
 
# Driver code



# Driver code

a = 3
m = 11
modInverse(a, m)
fermat_last_theorem(20,110)