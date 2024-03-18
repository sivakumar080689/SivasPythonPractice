


list_input = [40,3,27,66,1]
list_input2 = [9,3,45,8,21]
empty_list =[]
for i in list_input:
    if i % 2 == 0:
        empty_list.append(i)

print(empty_list)

#Using list comprehension

even_numbers =  [num for num in list_input2 if num % 2==0]
print(even_numbers)
