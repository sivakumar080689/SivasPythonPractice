#write a python program to check if a string contains any special character

import re

def check_special_char(in_str):
    #define a regular expression patterns to match special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

    if re.search(pattern, in_str):
        return  True
    else:
        return  False


#input a string

input_string = str(input("Enter a String: "))

#check if the string contains any special characters

contains_special = check_special_char(input_string)

if contains_special:
    print("The string contains special characters")
else:
    print("The string does not contain special characters")


