#write a program to find out the given number is positive or negative


input_num = int(input("Enter the num :"))

if input_num > 0:
    print(f"Number : {input_num} is positive ")
elif input_num == 0:
    print(f"Number : {input_num} is Zero ")
else:
    print(f"Number : {input_num} is negative ")