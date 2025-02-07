import time

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# DFS solution
def solve_n_queens_dfs(n):
    def dfs(row, board):
        if row == n:
            return [board[:]]  # Found a solution, return a copy of the board

        solutions = []
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solutions += dfs(row + 1, board)  # Recur to next row
                board[row] = -1  # Backtrack
        return solutions

    board = [-1] * n  # Board initialization
    return dfs(0, board)  # Start solving from the first row

# BFS solution
def solve_n_queens_bfs(n):
    queue = [(0, [-1] * n)]  # Start with row 0 and an empty board
    solutions = []

    while queue:
        row, board = queue.pop(0)  # Process the first element in the queue
        if row == n:
            solutions.append(board[:])  # If all queens are placed, store the solution

        for col in range(n):
            if is_safe(board, row, col, n):
                new_board = board[:]  # Make a copy of the current board
                new_board[row] = col  # Place the queen
                queue.append((row + 1, new_board))  # Move to the next row
    return solutions

def print_board(board, n):
    result = []
    for row in range(n):
        temp = ["0"] * n
        temp[board[row]] = "1"
        result.append(" ".join(temp))
    return "\n".join(result)

def main():
    while True:
        try:
            n = int(input("Enter N (>8) for the N-Queens problem: "))
            if n > 8:
                break
            else:
                print("Please enter a value greater than 8.")
        except ValueError:
            print("Invalid input. Please enter an integer greater than 8.")
            
    # Measure time for DFS
    start_time = time.time()
    print(f"\nSolving with DFS for {n}-Queens...")
    dfs_solutions = solve_n_queens_dfs(n)
    dfs_time = time.time() - start_time
    print(f"DFS found {len(dfs_solutions)} solution(s) in {dfs_time:.4f} seconds.")
    for solution in dfs_solutions[:2]:  # Display only first 2 solutions
        print(print_board(solution, n))
        print()

    # Measure time for BFS
    start_time = time.time()
    print(f"\nSolving with BFS for {n}-Queens...")
    bfs_solutions = solve_n_queens_bfs(n)
    bfs_time = time.time() - start_time
    print(f"BFS found {len(bfs_solutions)} solution(s) in {bfs_time:.4f} seconds.")
    for solution in bfs_solutions[2:4]:  # Display only first 2 solutions
        print(print_board(solution, n))
        print()

if __name__ == "__main__":
    main()

