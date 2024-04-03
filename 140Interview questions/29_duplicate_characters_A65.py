#Write a Python program to find all duplicate characters in string.

def find_duplicates(input_str):
    #create an empty dictionary to store character counts
    char_count = {}

    #Initialize a list to store duplicate characters
    duplicates = []

    #Iterate through each character in the input_string
    for i in input_string:
        #if the character is already in the dictionary, increment its
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    #Iterate through the dictionary and add characters with count >1
    for i, count in char_count.items():
        if count >1:
            duplicates.append(i)

    return duplicates

#input a string
input_string = "piyush sharma"

#find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)

print("Duplicate characters:",duplicate_chars)
