from pysat.formula import CNF
from pysat.solvers import Cadical195


def create_sudoku(size)->CNF:
    cnf = CNF()
    one_number_each(cnf, size)
    add_row_clauses(cnf, size)
    add_column_clauses(cnf, size)
    if size == 4:
        add_grid_clauses(cnf, 2, 2)
    elif size == 6:
        add_grid_clauses(cnf, 3, 2)
    elif size == 9:
        add_grid_clauses(cnf, 3, 3)

    return cnf


def one_number_each(cnf, size):
    #at least one number
    for i in range(1, size+1):
        for j in range(1, size+1):
                cnf.append([varnum(size, i, j, k) for k in range(1, size+1)])

    #at most one number
    for i in range(1, size+1):
        for j in range(1, size+1):
            for d1 in range(1, size):
                for d2 in range(d1+1, size+1):
                    cnf.append([-varnum(size, i, j, d1), -varnum(size, i, j, d2)])


def add_row_clauses(cnf, size):
    #at least every number in each row
    for r in range(1, size+1):
        for d in range(1, size+1):
            cnf.append([varnum(size, r, c, d) for c in range(1, size+1)])

    #at most every number per row
    for r in range(1, size+1):
        for d in range(1, size+1):
            for c1 in range(1, size):
                for c2 in range(c1+1, size+1):
                    cnf.append([-varnum(size, r, c1, d), -varnum(size, r, c2, d)])


def add_column_clauses(cnf, size):
    for c in range(1, size+1):
        for d in range(1, size+1):
            cnf.append([varnum(size, r, c, d) for r in range(1, size+1)])


    for c in range(1, size+1):
        for d in range(1, size+1):
            for r1 in range(1, size):
                for r2 in range(r1+1, size+1):
                    cnf.append([-varnum(size, r1, c, d), -varnum(size, r2, c, d)])


def add_grid_clauses(cnf, cblock_size, rblock_size):
    for br in range(0, cblock_size):
        for bc in range(0, rblock_size):
            for d in range(1, rblock_size*cblock_size+1):
                block_cells = [
                    varnum(cblock_size*rblock_size, r, c, d)
                    for r in range(1 + br * rblock_size, 1 + (br + 1) * rblock_size)
                    for c in range(1 + bc * cblock_size, 1 + (bc + 1) * cblock_size)
                ]
                cnf.append(block_cells)  # At least one must be true
                for i in range(len(block_cells)):
                    for j in range(i + 1, len(block_cells)):
                        cnf.append([-block_cells[i], -block_cells[j]])


def varnum(size, r, c, d):
    return size * size * (r - 1) + size * (c - 1) + d


def solve_sudoku(size, hints)->(CNF, list):
    sudoku = create_sudoku(size)
    add_sudoku_hints(sudoku, hints, size)
    solver = Cadical195(sudoku)
    if solver.solve():
        print(f"SAT: {size}x{size} Sudoku is solvable! {solver.time()}")
    else:
        print(f"SAT: {size}x{size} Sudoku has no solution found! {solver.time()}")
    return sudoku, solver.get_model()


def add_sudoku_hints(cnf, puzzle, size):
    for r in range(size):
        for c in range(size):
            if puzzle[r][c] != 0:  # If there is a clue
                cnf.append([varnum(size, r + 1, c + 1, puzzle[r][c])])


def check_uniqueness(cnf, model, size):
    negated_model = [-v for v in model if v > 0]
    cnf.append(negated_model)
    with Cadical195(cnf, True) as usolver:
        if usolver.solve():
            print(f"SAT: The {size}x{size} sudoku is not unique {usolver.time()}")
        else:
            print(f"SAT: The {size}x{size} sudoku is unique {usolver.time()}")


def compute_solution(model, size):
    solution = [[0] * size for _ in range(size)]
    for v in model:
        if v > 0:
            r = (v - 1) // (size * size) + 1
            c = ((v - 1) % (size * size)) // size + 1
            d = ((v - 1) % size) + 1
            if 1 <= r <= size and 1 <= c <= size and 1 <= d <= size:
                solution[r - 1][c - 1] = d
    return solution


def print_solution(solution):
    for row in solution:
        print(row)