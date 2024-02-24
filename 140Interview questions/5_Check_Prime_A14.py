
# Check the given  number is prime

#Prime  ---- a whole number greater than 1 that cannot be exactly divided by any whole number other
#than itself and 1 (e.g. 2, 3, 5, 7, 11).

#A prime number is a natural number greater than 1 which has only two factors, 1 & the number itself.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Take user input
input_num = int(input("Enter a number: "))

# Check if the input number is prime
if is_prime(input_num):
    print(f"{input_num} is a prime number.")
else:
    print(f"{input_num} is not a prime number.")
