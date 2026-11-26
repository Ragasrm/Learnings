# Question: 
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def compute_value(a):
    total = 0
    term = ""
    
    for i in range(1, 5):
        term += str(a)
        total += int(term)
        
    return total

if __name__ == "__main__":
    input_digit = input("Enter a digit: ")
    result = compute_value(input_digit)
    print(result)