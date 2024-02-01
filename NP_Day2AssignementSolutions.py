#1- write a program which takes single input from user contaning first name,last
#name and age as comma separated
#value and display then in 3 lines in given format below.


#example user input : Siva,Kumar,35

#output:
#First name is Ankit
#last name is Bansal
#Ankit is 35 years old

input = 'Siva,Kumar,35'

a =  input.split(",")

firstname = a[0]
lastname = a[1]
age = a[2]

print("First name is " + firstname )
print("last name is " + lastname )
print( firstname + " is " + age + " years old" )

#2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

#combined the 2 list and diplay the same without using extend method

#using extend
list1 = [1,3,4]
list2 = [2,4,6]

list1.extend(list2)

print(list1)

# without using extend
list3 = [1,3,4]
list4 = [2,4,6]
combined_list = list3 + list4
print("combined list: " , combined_list)


#3- given a list list1=[1,2,3,4,5,6,7,8]
#diplay a new list which contains only odd position index values from above list.

list1=[1,2,3,4,5,6,7,8]

odd_position_values = list1[1::2]

print(odd_position_values)

odd_position = []
for i in range(len(list1)):
    if i % 2 !=0:
        odd_position.append(list1[i])

print(odd_position)

#4- ipl= ['CSK','MI','KKR','LSG','PBKS']

#take a ipl team name as input from user and display a list of all elements from that name.

#example : input : KKR
#output : ['KKR','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']

a = input("enter a ipl team: ")
team_index=ipl.index(a)
print(ipl[team_index:])


#5- ipl= ['CSK','MI','KKR','LSG','PBKS']

#take a ipl team name as input from user and display a list of all elements except input one

#example : input : KKR
#output : ['CSK','MI','LSG','PBKS']

ipl = ['CSK','MI','KKR','LSG','PBKS']

input_team = input("Enter input team name: ")
ipl.remove(input_team)
print(ipl)

ipl1 =['CSK','MI','KKR','LSG','PBKS']
input_team1 = input("Enter input team name: ")
d=ipl1.index(input_team1)
ipl1.pop(d)
print(ipl1)


#6- ipl= ['CSK','MI','KKR','LSG','PBKS']
#take a user input contains 2 comma seprated values index,new_team .
# replace the index element of list with new value and display the same

#example : input : 2,SRH
#output : ['CSK','MI','SRH','LSG','PBKS']


ipl= ['CSK','MI','KKR','LSG','PBKS']

inputname_index = input("enter the index and new team(comma-separated): ")
index, new_team = inputname_index.split(',')

index = int(index)
ipl[index] = new_team

print(ipl)


#7- ipl= ['CSK','MI','KKR','LSG','PBKS']
#take ipl team name as user input. display True if the team exists else display False.

ipl= ['CSK','MI','KKR','LSG','PBKS']

iplname = input("enter input name: ")

if iplname in ipl:
    print("True")
else:
    print("False")


#8-ipl= ['CSK','MI','KKR','LSG','PBKS']
#take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list.
#Display the old list , new list,length of original and new list

#example : input : 2,SRH
#output :
#old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
#new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6

ipl= ['CSK','MI','KKR','LSG','PBKS']
user_input = input("Enter the index and new team (comma separated): ")
index, new_team = user_input.split(',')

index = int(index)

# display the old list and length
print("old list: ", ipl)
print("length of the original list:", len(ipl))

#add the new item at specified index
ipl.insert(index,new_team)

#display the new list and length

print("new list: ", ipl)
print("length of the new list:", len(ipl))






