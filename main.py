def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, row, n):
    if row == n:
        # Solution found, print board
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        print()
        return True  # Exit the recursive call when a solution is found
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1, n):
                return True  # Exit the recursive call when a solution is found
            board[row][col] = '.'  # Backtrack

def eight_queens():
    n = 8  # Board size and number of queens
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

# Run the solver
eight_queens()