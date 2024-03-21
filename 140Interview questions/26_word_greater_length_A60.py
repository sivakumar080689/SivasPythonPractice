#Write a Python program to find words which are greater than given length k.

def find_length(l,input):
    empty_list = []
    for i in input_words:
        if len(i) > input:
            empty_list.append(i)


    return empty_list


input_words =["apple","banana","mango","pine apple","jackfruit","pomegranate"]
length_input = 5
a = find_length(input_words,length_input)
print(a)