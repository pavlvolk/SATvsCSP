from pysat.formula import CNF
from pysat.solvers import Cadical195


def create_sudoku(size)->CNF:
    cnf = CNF()
    one_number_each(cnf, size)
    add_row_clauses(cnf, size)
    add_column_clauses(cnf, size)
    add_grid_clauses(cnf, size)

    return cnf


def one_number_each(cnf, size):
    #at least one number
    for i in range(1, size+1):
        for j in range(1, size+1):
                cnf.append([varnum(i, j, k) for k in range(1, size+1)])

    #at most one number
    for i in range(1, size+1):
        for j in range(1, size+1):
            for d1 in range(1, size):
                for d2 in range(d1+1, size+1):
                    cnf.append([-varnum(i, j, d1), -varnum(i, j, d2)])


def add_row_clauses(cnf, size):
    #at least every number in each row
    for r in range(1, size+1):
        for d in range(1, size+1):
            cnf.append([varnum(r, c, d) for c in range(1, size+1)])

    #at most every number per row
    for r in range(1, size+1):
        for d in range(1, size+1):
            for c1 in range(1, size):
                for c2 in range(c1+1, size+1):
                    cnf.append([-varnum(r, c1, d), -varnum(r, c2, d)])


def add_column_clauses(cnf, size):
    for c in range(1, size+1):
        for d in range(1, size+1):
            cnf.append([varnum(r, c, d) for r in range(1, size+1)])


    for c in range(1, size+1):
        for d in range(1, size+1):
            for r1 in range(1, size):
                for r2 in range(r1+1, size+1):
                    cnf.append([-varnum(r1, c, d), -varnum(r2, c, d)])


def add_grid_clauses(cnf, size):
    for br in range(0, 3):
        for bc in range(0, 3):
            for d in range(1, 10):
                block_cells = [
                    varnum(r, c, d)
                    for r in range(1 + br * 3, 4 + br * 3)
                    for c in range(1 + bc * 3, 4 + bc * 3)
                ]
                cnf.append(block_cells)  # At least one must be true
                for i in range(len(block_cells)):
                    for j in range(i + 1, len(block_cells)):
                        cnf.append([-block_cells[i], -block_cells[j]])


def varnum(r, c, d):
    return 81 * (r - 1) + 9 * (c - 1) + d


def add_sudoku_hints(cnf, puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:  # If there is a clue
                cnf.append([varnum(r + 1, c + 1, puzzle[r][c])])


def solve_sudoku(size, hints):
    sudoku = create_sudoku(size)
    add_sudoku_hints(sudoku, hints)
    solver = Cadical195()
    if solver.solve(sudoku):
        print("Sudoku is solvable")
    else:
        print("No solution found!")


def add_sudoku_hints(cnf, puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:  # If there is a clue
                cnf.append([varnum(r + 1, c + 1, puzzle[r][c])])


def check_uniqueness(cnf, solver):
    model = solver.get_model()
    cnf.append([-model[i] for i in range(0, 729)])
    with Cadical195(cnf) as usolver:
        if usolver.solve():
            print("The sudoku is not unique")
        else:
            print("The sudoku is unique")
