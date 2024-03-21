


#Write a Python program to Cloning or Copying a list.
#using the slice operator

original_list = [1,2,3,4,5]
copy_list = original_list[:]
print(copy_list)

#using the list constructor

original_list_2 = [6,7,8]
copy_list_2 = list(original_list_2)
print(copy_list_2)

#using the list comprehension
original_list_3 = [9,0]
copy_list_3 = [i for i in original_list_3]
print(copy_list_3)