#Write a Python program for removing 𝑖 character from a string.
def remove_char(instring,position):
    if position <0 or position >= len(input_string):
        print(f"Invalid index")
        return instring
    return instring[:position] + instring[position + 1:]


input_string ='Hello world'
remove_char_pos= 7

a = remove_char(input_string,remove_char_pos)
print(a)