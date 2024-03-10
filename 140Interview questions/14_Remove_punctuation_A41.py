punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str =input("Enter a string")

#remove punctuation from the string

no_punct = ""
for i in my_str:
    if i not in punctuation:
        no_punct = no_punct + i


print(no_punct)

