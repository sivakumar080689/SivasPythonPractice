#
# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter)
# and prints the BMI in the output.

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = weight / (height ** 2)

print("Your BMI is :", bmi )

# ****************************************************

# write a program to which takes the name of the user as input
# and replace all the occurence of character 'a' in the name to 'b' and print it.

name = input("Enter your name:")
new_name = name.replace('a','b')
print("Modified name:", new_name)

# ****************************************************

# write a program which takes 2 inputs from user as principal amount (int)
# and rate of interest (float) and print the expected total amount

#example principal 100 interest percent 10 then amount after 2 years will be : 100*1.1*1.1 = 121

principal = int(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))

total_amount =  principal * (1  + (interest_rate/100)) **2

print("Expected total amount after 2 years: ", total_amount)

# ****************************************************

# writing program which takes city name from user input. irrespective of in which case
# users enters the city name, print the city name in camel case meaning first letter
# should be capital and rest in small

#example -> input : MYSORE, print -> Mysore

city_name = input("Enter city name: ")

city_name = city_name.lower()

city_name = city_name[0].upper() + city_name[1:]

print(city_name)

# ****************************************************
#5- write a program which takes the name of the user as input and print the index of
# character 'a' in the string.if 'a' is not there then return -1.

name = input("Enter input name: ")
index = name.find('a')

print("Index of a:",str(index))

#6-  Display the number of letters in the below string

myword = "origamiismypassion"

print(len(myword))

#7- take 3 inputs from user : first name , last name and age . Display the information
#in below format

firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = input("Enter age: ")
print("My Name is "+ firstname.capitalize() + lastname.capitalize()+ ". I am "+age+" years old.")


#8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
#example


firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
company = input("Enter company: ")

formatted_firstname =firstname[0:2].lower()
formatted_lastname=lastname[-3:].lower()

print("Email: "+formatted_firstname+formatted_lastname+"@"+company+".com")