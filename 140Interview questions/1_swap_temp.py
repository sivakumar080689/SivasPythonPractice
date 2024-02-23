#Write a Python program to swap two variables.


a = input("enter the a :")
b = input("enter the b :")

print(f"Original Values: a={a}, b={b}")

temp = a
a=b
b=temp

print(f"Swapped Values: a={a},b={b}")
