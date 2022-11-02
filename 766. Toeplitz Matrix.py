
def isToeplitzMatrix(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    for col in range(len(matrix[0])-1):
        current_row = 0
        current_col = col
        while current_row < nrow-1 and current_col < ncol-1:
            diagonal_element_1 = matrix[current_row][current_col]
            diagonal_element_2 = matrix[current_row+1][current_col+1]
            if diagonal_element_1 != diagonal_element_2:
                return False
            current_row += 1
            current_col += 1
            
    for row in range(len(matrix)-1):
        current_row = row
        current_col = 0
        while current_row < nrow-1 and current_col < ncol-1:
            diagonal_element_1 = matrix[current_row][current_col]
            diagonal_element_2 = matrix[current_row+1][current_col+1]
            if diagonal_element_1 != diagonal_element_2:
                return False
            current_row += 1
            current_col += 1
    return True


print(isToeplitzMatrix([[84]]))