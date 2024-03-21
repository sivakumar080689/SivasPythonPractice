#Write a Python program to Count occurrences of an element in a list.

def count_occurence(l,elementcount):
    a = l.count(elementcount)
    return a

list_element = [1,2,5,3,2,2,7,4,3,4,0,0,0,9,1]
element_to_count = 0

a = count_occurence(list_element,element_to_count)

print(a)