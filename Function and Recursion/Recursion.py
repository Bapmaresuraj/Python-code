
def factorial(n):
    """Write a function that calculates the factorial of a given number."""
    if n==1 or n==0: # Base case 
        return 1
    else:
        return n*factorial(n-1) # recursive case 
    


print(factorial(5))