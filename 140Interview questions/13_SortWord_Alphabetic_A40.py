
def sort_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Sort the words alphabetically
    sorted_words = sorted(words)

    return ' '.join(sorted_words)


# Example usage
input_string = input("Enter a string: ")
sorted_string = sort_words(input_string)
print("Sorted string:", sorted_string)
