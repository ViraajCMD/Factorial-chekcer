def factorial(x):
    '''This function is to find that factorial of the variable x'''

    if x == 0 or x==1:

        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)

print("\nThe factorial of 0:", factorial(0))
print("\nhe factorial of 1:", factorial(1))
print("\nThe factorial of 2:", factorial(2))
print("\nThe factorial of 5:", factorial(5))
print("\nThe factorial of 10:", factorial(10))