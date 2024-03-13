def find_n_largest_largest(listabc,input_num):
    sort_list = sorted(listabc,reverse=True)
    largest_elements = sort_list[0:input_num]
    return largest_elements


lst_custom = [30,9,12,4,5,47,63,8,55,88,55,0]

input_number = int(input("Enter no: "))

a = find_n_largest_largest(lst_custom,input_number)

print(a)