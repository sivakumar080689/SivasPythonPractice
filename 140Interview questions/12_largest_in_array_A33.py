
def check_largest(c):
    #initialize the first element as the largest
    largest_element = c[0]

    #iterate through the array to find the largest element
    for i in c:
        if i > largest_element:
            largest_element = i

    return largest_element

input_array = [1,4,6,8]
a= check_largest(input_array)
print(a)