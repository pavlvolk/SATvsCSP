import SudokuCSP
import SudokuSAT

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

cnf4, model4 = SudokuSAT.solve_sudoku(4, hints4)
SudokuSAT.check_uniqueness(cnf4, model4, 4)
cnf6, model6 = SudokuSAT.solve_sudoku(6, hints6)
SudokuSAT.check_uniqueness(cnf6, model6, 6)
cnf9, model9 = SudokuSAT.solve_sudoku(9, hints9)
SudokuSAT.check_uniqueness(cnf9, model9, 9)

task4 = SudokuCSP.solve_sudoku(4, "Solutions/", hints4)
SudokuCSP.check_uniqueness(task4, 4, hints4)
task6 = SudokuCSP.solve_sudoku(6, "Solutions/", hints6)
SudokuCSP.check_uniqueness(task6, 6, hints6)
task9 = SudokuCSP.solve_sudoku(9, "Solutions/", hints9)
SudokuCSP.check_uniqueness(task9, 9, hints9)

