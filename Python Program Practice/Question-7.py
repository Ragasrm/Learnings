# Question: 
# Write a program which takes 2 digits, X,Y as input and
# generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. 
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
# Example Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]

# Initialize an empty 2D list
matrix = []

# write the logic to generate the 2D array, in comprehension or nested loop

for i in range(rowNum):
    row=[]
    for j in range(colNum):
        row.append(i * j)
    matrix.append(row)

print(matrix)
