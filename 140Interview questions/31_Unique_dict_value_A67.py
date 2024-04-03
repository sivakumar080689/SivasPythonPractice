
# sample dictionary
my_dict = {
    'a' : 10,
    'b' : 20,
    'c' : 10,
    'd' : 30,
    'e' : 20
}

#Initialize an empty set to store unique values
uni_val = set()

#Iterate through the values of dictionary
for i in my_dict.values():
    #Add each value to the set
    uni_val.add(i)

unique_values_list = list(uni_val)

print(unique_values_list)

