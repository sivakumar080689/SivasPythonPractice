#sort by python dictionaries by Key or Value

#Write a Python program to sort Python Dictionaries by Key or Value
#sort by keys

sample_dict = {'apple':3,'cherry':2,'banana':1,'date':4}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))

for key,value in sorted_dict_by_keys.items():
    print(f"{key}:{value}")

#sort_by_values




