# Question: 
# Write a program that accepts a sentence and 
# calculate the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def count_case(sentence):
    upper_case_count = 0
    lower_case_count = 0
    
    for char in sentence:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
            
    return upper_case_count, lower_case_count

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    upper_count, lower_count = count_case(input_sentence)
    print(f"UPPER CASE {upper_count} LOWER CASE {lower_count}")