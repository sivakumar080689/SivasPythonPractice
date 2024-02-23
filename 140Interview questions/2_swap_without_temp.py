#Write a Python program to swap two variables without temp variable.

a = input("enter the a value :")
b = input("enter the b value :")

print(f"orginal values a={a}, b={b}")

a , b = b, a

print(f"swapped values a={a}, b={b}")

