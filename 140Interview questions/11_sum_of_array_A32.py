

def sum_of_element(my_list):
    total = 0
    for i in my_list:
        total += i
    return total

my_list = [1,2,3,4,1,2]
result = sum_of_element(my_list)
print(result)