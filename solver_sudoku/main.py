def valid_move(matrix, row, col, num):
    for x in range(9):
        if matrix[row][x] == num:
            return False
    for x in range(9):
        if matrix[x][col] == num:
            return False

    cornerRow = row - row%3
    cornerCol = col - col%3
     
    for x in range(3):
        for y in range(3):
            if matrix[cornerRow + x][cornerCol + y] == num:
                return False
    return True

def solve(matrix, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if matrix[row][col] > 0:
        return solve(matrix, row, col + 1)
    for num in range(1, 10):
        if valid_move(matrix, row, col, num):
            matrix[row][col] = num
            if solve(matrix, row, col +1):
                return True
        matrix[row][col] = 0
    return False

print("Enter the sudoku, in the blanks type '0': ")
matrix = [[0 for x in range(9)] for y in range(9)]
for i in range(9):
    c = input().split()
    c = [int(x) for x in c]
    for j in range(9):
        matrix[i][j] = c[j]

if solve(matrix, 0, 0):
    print("Your solution is: ")
    print("-------------------------")
    for x in range(9):
        for y in range(9):
            if y % 3 == 0:
                print("|", end=" ")
            print(matrix[x][y], end=" ")
        print("|", end=" ")
        print()
        if x % 3 == 2:
            print("-------------------------")

else:
    print("Sudoku cannot be solved")