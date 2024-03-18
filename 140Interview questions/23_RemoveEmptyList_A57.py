list_of_lists = [[1,2,3],[],[4,5],[],[6,7]]

#filtered_list = [i for i in list_of_lists if i]  this is another way
filtered_list=[]
for i in list_of_lists:
    if i:
        filtered_list.append(i)


print(filtered_list)