#1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.

#example :
#file 1:
#this is namaste sql course
#this is python course
#this assinment is part of day4 lecture


#file2:this is namaste sql course:5
#this is python course:4
#this assignment is part of day4 lecture:7

###*********Solution

# create the first file and write lines into it
with open('putheri1.txt','w') as putheri1:
    lines = [
        "Putheri is a village in Kanyakumari district, Tamil Nadu, India.",
        "The panchayat has total of seven panchayat constituencies",
        "pincode is 629 001"
    ]
    for line in lines:
        putheri1.write(line + '\n')

# Create the second file with word count at the end of each line
with open('putheri1.txt','r') as putheri1, open('erachakulam1.txt','w') as erachakulam1:
    for line in putheri1:
        line = line.strip()   # strip will remove trailing and leading spaces
        word_count = len(line.split())  # split method splits a string into list
        erachakulam1.write(line + ':' + str(word_count) + '\n')

print("File creation and word count operation completed:")


#pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly, then repeatedly ask them
#for the capital until they either enter the correct answer or type "exit".
#If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
#the correct answer and the word "Goodbye".
#
#Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver" is the same as "denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".
#



capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state = input("pick a state from dictionary: ")
state = state.capitalize()

# for loop is used for iterating over a sequence
# while loop will execute set of statements as long as condition is true
while True:
    if state in capitals_dict:
        capital = capitals_dict[state]
        guess = input("Enter the capital of {}:".format(state))
        guess = guess.capitalize()

        if guess == capital:
            print("Correct !")
            break
        elif guess.lower() == 'exit':
            print("The correct answer was: {}".format(capital))
            print("Goodbye!")
            break
        else:
            print("Incorrect. Tray again or type 'exit' to quit.")
    else:
        print("Invalid state. Please pick a state from the dictionary")
    state = input("pick a state from dictionary: ")
    state = state.capitalize()

#3- write a program to take state as input from user and print the capital of the state using above dictonary.
#If the state is not there in dictonary then print "sorry , information not available"


capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state = input("Enter the state: ")
capital = capitals_dict.get(state.capitalize())

if capital:
    print(" {} is the capital of {}".format(capital,state))
else:
    print("Wrong information")


















