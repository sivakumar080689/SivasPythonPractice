#1- given a list of numbers, write a program to find the mean of the numbers in list

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the mean of the numbers
total = sum(numbers)
mean = total / len(numbers)

# Display the mean
print("Mean:", mean)



#2- given a list of numbers unsorted, write a program to find the median of the numbers in list


#Example list of numbers
population = [2,1,8,9]

#sort the list in ascending order

population.sort()

#Calculate the median

length = len(population)

if length % 2 == 0:
    median = (population[length//2 - 1] + population[length//2]) / 2
else:
    median = population[length//2]

print(median)

#3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers

numbers = [1,2,3,4]
even_number = []
odd_number = []

for i in numbers:
    if i%2==0:
        even_number.append(i)
    else:
        odd_number.append(i)

print(even_number)
print(odd_number)


#loop from 0 to 9


for index in range(9):
    patientId = 10 + index
    t = (patientId, f"Patient {patientId}", "phoenix")
    print(t)



#4- create a dictionary to store following attributes of CSK
#key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players),
#oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss




#4- create a dictionary to store following attributes of CSK
#key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players), oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss


csk = {
    "team_name": "Chennai Super Kings",
    "captain": "MS Dhoni",
    "playing_11": [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    "opponents": ["MI", "RCB", "GT"],
    "results": ["Won", "Loss", "Won"]
}
print(csk)

#5- in the previous dictonary add one more item for RCB. you can choose any 3 opponents.

IPL = {"CSK":{
    "team_name": "Chennai Super Kings",
    "captain": "MS Dhoni",
    "playing_11": [
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
        ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
    ],
    "opponents": ["MI", "RCB", "GT"],
    "results": ["Won", "Loss", "Won"]
},
    "RCB":{
        "team_name": "Royal Challengers Bangalore",
        "captain": "Virat Kohli",
        "playing_11": [
            ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 1
            ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 2
            ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11"],  # Match 3
        ],
        "opponents": ["MI", "CSK", "GT"],
        "results": ["Loss", "Loss", "Loss"]
    }

}

print(IPL)

#6- write a program to take a positive number as input from user. if the user enters
#negative number then keep promting him to enter positive number until he enters the positive
#number and then print the same:

number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid input, Please enter a positive number: ")
    number = int(input("Enter a positive number: "))

print("The positive number you entered is: ", number)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6,16,2):
    print(x)


adj =["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)



universities =[
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
empty_list = []

#list of all university
for i in universities:
    empty_list.append(i[0])
print("List of all universitynames : ", empty_list)

#total no of students

total_students = 0

for i in universities:
    total_students =  total_students +  i[1]
print("Total no of students: ", total_students)

#Mean of tuition fees

tuition_fees = []
for i in universities:
    tuition_fees.append(i[2])
mean_tuition = sum(tuition_fees)/len(tuition_fees)
print("mean_tuition_fee: ", mean_tuition)

universities =[
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

universities_dict = {}
for i in universities:
    name  = i[0]
    attributes = {
        'total_students' :i[1],
        'tuition_fees' : i[2]
    }

    universities_dict[name] = attributes

print(universities_dict)


# reverse a string
string = input("Enter a string : ")

reversed_string = ""
for i in string:
    reversed_string = i + reversed_string

print('method 1')
print(reversed_string)

print("method 2")
reversed_string_2 = string[::-1]
print(reversed_string_2)

#10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
#solution:
#method 1 using sorting
a =[6,5,1,113]

a.sort()
print(a[-1])



#method 2

largest_number = a[0]

for i in a:
    if i > largest_number:
        print(i)
        largest_number = i

print("Largest number : ", largest_number)








