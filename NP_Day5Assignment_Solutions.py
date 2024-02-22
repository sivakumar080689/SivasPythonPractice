#iterative approach
def fact_iterative(n):
    if n < 0:
        return "dont give negative"
    elif n== 0:
        return 1
    else:
        result =1
        for i in range(1, n+1):
            result = result * i
        return result

print(fact_iterative(4))


def fact_recursive(n):
    if n < 0:
        return "dont give negative"
    elif n== 0:
        return 1
    else:
        return n * fact_recursive(n-1)

print(fact_recursive(5))



#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

a = input("Enter the input string: ")

def upperlowercount(a):
    upper_count = 0
    lower_count = 0
    for i in a:
        if i.isupper():
            upper_count +=1
        elif i.islower():
            lower_count +=1

    return upper_count, lower_count



upper,lower = upperlowercount(a)

print("No of upper case characters: ", upper)
print("No of lower case characters: ",lower)

######################
def get_unique_list(listdef):
    unique_list = []

    for i in listdef:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

result = get_unique_list(listabc)
print("Unique list: ",result)



#palindrome
def is_palindrome(string):
    string = string.lower()
    reversed_string = string[::-1]
    return string == reversed_string

input_string = input("Enter a string : ")

if is_palindrome(input_string):
    print("The string is palindrome")
else:
    print("The string is not a palindrome")



#7- write a python function that accepts a string and prints the count of occurence of each characters
#sample string: aabccda
#expected result:
#a -> 3
#b-> 1
#c-> 2
#d -> 1

def count_characters(string):
    count_char = {}
    for i in string:
        if i in count_char:
            count_char[i] += 1
        else:
            count_char[i] = 1

    for i,count in count_char.items():
        print(i,"->",count)


input_string = input("Enter a string :")
count_characters(input_string)



#6- Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow


sequence = input("Enter a hyphen-separated words: ")
words = sequence.split('-')

sortedwords = sorted(words)
print(sortedwords)

result = '-'.join(sortedwords)
print(result)

sequence = input("Enter the dsfs :")
words = sequence.split('-')

sorted_words = sorted(words)

result = ''

for i in sorted_words:
    result += i + '-'

result = result.rstrip('-')

print(result)


#8- write a function called is_prime that takes an integer as an argument and returns True if it is a prime number, and False otherwise.

def is_prime(number):
    if number <=1:
        return  False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True



input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print("The number is prime")
else:
    print("The number is not prime")


#9- write a function called generate_fibonacci that takes an integer n as input and returns a list of the first n Fibonacci numbers.

def generate_fibonacci(n):
    fibonacci_sequence = []

    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)

    for i in range(2,n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

    return fibonacci_sequence


input_n = int(input("Enter a number :"))
fibonacci_numbers =  generate_fibonacci(input_n)
print(fibonacci_numbers)



#10- Write a function called capitalize_odd_letters that takes a string as input and returns the same string with the odd-indexed letters capitalized.


def capitalize_odd_letters(string):
    capitalized_string = ""

    for i in range(len(string)):
        if i % 2 == 1:
            capitalized_string += string[i].upper()
        else:
            capitalized_string += string[i]

    return capitalized_string

input_string = input("Enter a string : ")
result = capitalize_odd_letters(input_string)
print("Modified String:", result)


#11- write a function called find_common_elements that takes two lists as input and returns a new list containing the common elements between the two lists.

def find_common_elements(list1, list2):

    common_elements = []

    for i in list1:
        if i in list2:
            common_elements.append(i)

    return common_elements


input_list1 = [1,2,3,4]
input_list2 = [3,4,5,6]
result = find_common_elements(input_list1,input_list2)
print("common elements:" , result)





