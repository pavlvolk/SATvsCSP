import math

import CSP_Solver as CS

def create_sudoku(size)->CS:
    cells = size*size
    task = CS.CSP(variables=cells)
    task.commonDomain(domain=[i for i in range(1, size+1)])

    add_row_constraints(task, size)
    add_col_constraints(task, size)
    add_subgrid_constraints_4x4(task)
    return task


def add_row_constraints(task, size):
    for row in range(0, size):
        for i in range(1, size):
            for j in range(i+1, size+1):
                task.addConstraint("value["+str(i+row*size)+"] != value["+str(j+row*size)+"]")
                #print("value["+str(i+row*size)+"] != value["+str(j+row*size)+"]")


def add_col_constraints(task, size):
    for col in range(1, size+1):
        for i in range(0, size):
            for j in range(i+1, size):
                task.addConstraint("value[" + str(col + i*size) + "] != value[" + str(col + j*size) + "]")
                #print("value[" + str(col + i*size) + "] != value[" + str(col + j*size) + "]")


#Only works for grids that are square numbers
def add_subgrid_constraints_9x9(task, size):
    sub_grid_size = 3
    for grid in range(0, sub_grid_size):
        for i in range(0, sub_grid_size):
            for j in range(0, sub_grid_size):
                a=""


def add_subgrid_constraints_4x4(task):
    sub_grid_size = 2
    for vertical_grid in range(0, sub_grid_size):
        for grid in range(0, sub_grid_size):
            ul = 1 + vertical_grid * 4 + sub_grid_size * grid
            lr = ul + 5
            ur = ul + 1
            ll = ul + 4
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lr) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(ll) + "]")


def add_subgrid_constraints_6x6(task, size):
    sub_grid_size = 3
    for vertical_grid in range(0, sub_grid_size):
        for grid in range(0, sub_grid_size):
            ul = 1 + vertical_grid * 4 + sub_grid_size * grid
            lr = ul + 5
            ur = ul + 1
            ll = ul + 4
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lr) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(ll) + "]")


task = create_sudoku(4)

task.solve_BackTrack(timeout=10)

for i in range(1, 17):
        print(f"Cell {i}: {task.value[i]}")