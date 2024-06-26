def prime(n):
    """Function to check if a number is prime."""

    # Prime numbers are greater than 1
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found a factor, hence not prime

    return True  # No factors found other than 1 and itself, so prime


# Test the function
num = int(input("Enter a number to check if it's prime: "))
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
