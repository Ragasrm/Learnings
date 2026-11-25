# Question: 
# Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: 
# hello world! 123 
# Then, the output should be: LETTERS 10 DIGITS 3

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def count_letters_digits(sentence):
    d = { "DIGITS":0, "LETTERS":0, "SPECIAL": 0 }
    for w in sentence:
        if w.isdigit():
            d["DIGITS"]+=1
        elif w.isalpha():
            d["LETTERS"]+=1
        else:
            d["SPECIAL"]+=1
    
    return d



print("Answer:-->", count_letters_digits(input("Enter a sentence \n ")))