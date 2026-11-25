# Question: 
# Write a program that accepts a sequence of whitespace separated words as input and
#  prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, 
# the output should be: again and hello makes perfect practice world

# Hints: 
# In case of input data being supplied to the question, 
# it should be assumed to be a console input. We use set container to remove duplicated data automatically and
#  then use sorted() to sort the data.



def remove_duplicates_and_sort(input_string):
    # split into []
    splited_list = input_string.split(" ");
    # sort to order it
    splited_list.sort()
    # set for remove dublicate word
    unique_words = set(splited_list)
    return " ".join(sorted(unique_words))

print("Answer:-->", remove_duplicates_and_sort("hello world and practice makes perfect and hello world again"))