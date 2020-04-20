def used_in_row(arr,row,num):
    count = 0
    for i in range(9): 
        if(arr[row][i] == num):
            count += 1
    
    if count > 1:
        return True
    return False

def used_in_col(arr,col,num):
    count = 0
    for i in range(9): 
        if(arr[i][col] == num): 
            count += 1
    if count > 1:
        return True
    return False

def used_in_box(arr,row,col,num):
    count = 0
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                count += 1
    if count > 1:
        return True
    return False


def check_location_is_safe(arr,row,col,num): 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 


def is_sudoku_valid(arr): 
    for i in range(9):
        for j in range(9):
            if not check_location_is_safe(arr,i,j,arr[i][j]):
                return False
    return True

if __name__=="__main__": 

    grid=[[0 for x in range(9)]for y in range(9)] 
    
    grid=[[2, 1, 4, 3, 5, 7, 9, 6, 8], 
            [3, 7, 6, 9, 4, 8, 5, 1, 2], 
            [5, 8, 9, 6, 2, 1, 4, 3, 7], 
            [4, 6, 3, 5, 1, 2, 7, 8, 9], 
            [9, 2, 7, 8, 6, 3, 1, 4, 5], 
            [8, 5, 1, 7, 9, 4, 6, 2, 3], 
            [1, 3, 8, 4, 7, 9, 2, 5, 6], 
            [6, 9, 2, 1, 3, 5, 8, 7, 4], 
            [7, 4, 5, 2, 8, 6, 3, 9, 1]]
    
    if(is_sudoku_valid(grid)): 
        print("Sudoku is valid")
    else: 
        print("Sudoku is invalid")
