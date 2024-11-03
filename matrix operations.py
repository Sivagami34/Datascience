rows = int(input("Enter number of rows for the matrix: "))
columns = int(input("Enter number of columns for the matrix: "))
matrix1 = []
for r in range(rows):
    row = []
    for n in range(columns):
        v = int(input("Enter the value: "))
        row.append(v)
    matrix1.append(row)
print(matrix1)

matrix2 = []
for i in range(rows):
    roww = []
    for i in range(columns):
        v1 = int(input("Enter the value: "))
        roww.append(v1)
    matrix2.append(roww)
print(matrix2)