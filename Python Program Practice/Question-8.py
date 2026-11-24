# Question: 
# Write a program that accepts a comma separated sequence of words as input and
#  prints the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the following input is supplied to the program: without,hello,bag,world 
# Then, the output should be: bag,hello,without,world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.



def sort_words(words: str) -> str:
    # Step 1: Split comma-separated string into a list
    result = words.split(",")

    # Step 2: Remove unwanted spaces from each word
    cleaned_words = []

    for word in result:
        cleaned_words.append(word.strip())

    # Step 3: Sort alphabetically (case-insensitive)
    cleaned_words.sort(key=str.lower)

    # Step 4: Join the sorted words into a comma-separated string
    return ", ".join(cleaned_words)


# Get input and display output
answer = sort_words(input("Enter comma-separated words:\n"))
print("Answer:", answer)