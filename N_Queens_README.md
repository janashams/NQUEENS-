
# README

## N-Queens Problem Implementation

This project provides a Python implementation of the N-Queens problem using both Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms. The program computes all valid arrangements of N queens on an N×N chessboard such that no two queens threaten each other.

---

### How It Works

#### Core Functionality
1. **is_safe(board, row, col, n):**
   - Checks if placing a queen at position `(row, col)` is valid.
   - Ensures no other queen is placed in the same column or diagonal.

2. **solve_n_queens_dfs(n):**
   - Implements the DFS algorithm to find solutions recursively.
   - Uses backtracking to explore all possible configurations.

3. **solve_n_queens_bfs(n):**
   - Implements the BFS algorithm to find solutions iteratively.
   - Processes row-by-row by enqueuing board states.

4. **print_board(board, n):**
   - Converts a board configuration into a human-readable format.
   - "1" indicates the presence of a queen, and "0" indicates an empty cell.

5. **main():**
   - Serves as the entry point for the program.
   - Prompts the user for input (N > 8).
   - Solves the N-Queens problem using both DFS and BFS.
   - Measures and compares execution times.

---

### Features
- **DFS Implementation:** Uses recursion and backtracking to explore all possible solutions.
- **BFS Implementation:** Uses a queue to iteratively explore all possible solutions.
- **Performance Comparison:** Reports the number of solutions found and the time taken for both DFS and BFS.
- **Solution Display:** Displays the first two solutions from DFS and the next two solutions from BFS.

---

### Sample Output
```
Enter N (>8) for the N-Queens problem: 9

Solving with DFS for 9-Queens...
DFS found 352 solution(s) in 0.0342 seconds.
1 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0
...

Solving with BFS for 9-Queens...
BFS found 352 solution(s) in 0.0485 seconds.
0 0 0 0 1 0 0 0 0
...
```

---

### Notes
- The DFS algorithm typically performs faster than BFS for this problem due to its recursive nature and early backtracking.
- Ensure N is large enough (>8) to observe meaningful performance differences between DFS and BFS.

---

### Author
This project was developed to illustrate the differences between DFS and BFS approaches for solving combinatorial problems.
