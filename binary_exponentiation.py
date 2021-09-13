def binary_exponentiation(x,n,m):
    if(n == 0):
        return 1
    elif(n%2 == 0): # IF n is even 
        return binary_exponentiation(x**2 % m, n/2, m)
    else: # if n is odd 
        return (x * binary_exponentiation(x**2 % m, (n-1)/2, m)) % m  
    
def binary_exponentiation_it(x,n,m):
    result = 1
    while(n > 0):
        if(n%2 == 1):   # if n is odd 
            result = (result*x) % m 
        x = x**2 % m
        n //= 2
    return result

x = binary_exponentiation(3,10,51)
print(x)