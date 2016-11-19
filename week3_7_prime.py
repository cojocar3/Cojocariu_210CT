def prime(n,a=1):       # def the function with first argument ,number to be checked, and second argument,start point for verification
    if a == n:          # if start point gets equal to number , number is prime
        return "prime"
    else:               # if number divides to another number than 1 is not prime 
        if n%a == 0 and a != 1:     
            return "not prime"
        else:
            return prime(n,a+1)     # increase starting point by 1 
