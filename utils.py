def num_digits(num):
    digit_count = 0
    while(num != 0):
        digit_count += 1
        num //= 10
    return digit_count

def get_digit(num,place):
    return int((num/place) % 10)

def cum_sum(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr 

def binary_exponentiation(x,n):
    if(n == 0):
        return 1
    elif(n%2 == 0): # IF n is even 
        return binary_exponentiation(x**2,n/2)
    else: # if n is odd 
        return x * binary_exponentiation(x**2,(n-1)/2)
    
def binary_exponentiation_it(x,n):
    result = 1
    while(n > 0):
        if(n%2 == 1):   # if n is odd 
            result *= x
        x = x**2
        n //= 2
    return result