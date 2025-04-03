from SudokuSAT import solve_sudoku, check_uniqueness, print_solution, compute_solution

hints4 = [[0, 0, 0, 3],
          [0, 4, 0, 0],
          [1, 0, 0, 4],
          [0, 0, 3, 0]]

hints6 = [[6, 2, 0, 5, 0, 3],
          [0, 0, 0, 0, 0, 0],
          [5, 0, 0, 0, 3, 0],
          [0, 6, 0, 0, 2, 0],
          [0, 0, 0, 3, 4, 6],
          [3, 0, 6, 0, 0, 0],]

hints9 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

cnf4, model4 = solve_sudoku(4, hints4)
check_uniqueness(cnf4, model4, 4)
cnf6, model6 = solve_sudoku(6, hints6)
check_uniqueness(cnf6, model6, 6)
cnf9, model9 = solve_sudoku(9, hints9)
check_uniqueness(cnf9, model9, 9)

print_solution(compute_solution(model4, 4))
print_solution(compute_solution(model6, 6))
print_solution(compute_solution(model9, 9))