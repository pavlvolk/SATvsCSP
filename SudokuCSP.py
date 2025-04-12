import time

import CSP_Solver as CS


def create_sudoku_csp(size, path)->CS:
    cells = size*size
    task = CS.CSP(variables=cells, solution_path=path)
    task.commonDomain(domain=[i for i in range(1, size+1)])

    add_row_constraints(task, size)
    add_col_constraints(task, size)
    if size == 4:
        add_subgrid_constraints_4x4(task)
    elif size == 6:
        add_subgrid_constraints_6x6(task)
    elif size == 9:
        add_subgrid_constraints_9x9(task)
    else:
        print("Invalid size; Returning Latin Square")
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
def add_subgrid_constraints_9x9(task):
    sub_grid_size = 3
    for vertical_grid in range(0, sub_grid_size):
        for grid in range(0, sub_grid_size):
            ul = 1 + vertical_grid*27 + grid*3
            uc = ul + 1
            ur = ul + 2
            cl = ul + 9
            cc = ul + 10
            cr = ul + 11
            ll = ul + 18
            lc = ul + 19
            lr = ul + 20

            #Constraints for ul
            task.addConstraint("value[" + str(ul) + "] != value[" + str(cc) + "]")
            task.addConstraint("value[" + str(ul) + "] != value[" + str(cr) + "]")
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lc) + "]")
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lr) + "]")

            # Constraints for uc
            task.addConstraint("value[" + str(uc) + "] != value[" + str(cl) + "]")
            task.addConstraint("value[" + str(uc) + "] != value[" + str(cr) + "]")
            task.addConstraint("value[" + str(uc) + "] != value[" + str(ll) + "]")
            task.addConstraint("value[" + str(uc) + "] != value[" + str(lr) + "]")

            # Constraints for ur
            task.addConstraint("value[" + str(ur) + "] != value[" + str(cl) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(cc) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(ll) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(lc) + "]")

            # Constraints for cl
            task.addConstraint("value[" + str(cl) + "] != value[" + str(lc) + "]")
            task.addConstraint("value[" + str(cl) + "] != value[" + str(lr) + "]")

            # Constraints for cc
            task.addConstraint("value[" + str(cc) + "] != value[" + str(ll) + "]")
            task.addConstraint("value[" + str(cc) + "] != value[" + str(lr) + "]")

            # Constraints for cr
            task.addConstraint("value[" + str(cr) + "] != value[" + str(ll) + "]")
            task.addConstraint("value[" + str(cr) + "] != value[" + str(lc) + "]")


def add_subgrid_constraints_4x4(task):
    for vertical_grid in range(0, 2):
        for grid in range(0, 2):
            ul = 1 + vertical_grid * 8 + 2 * grid
            lr = ul + 5
            ur = ul + 1
            ll = ul + 4
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lr) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(ll) + "]")


def add_subgrid_constraints_6x6(task):
    for vertical_grid in range(0, 3):
        for grid in range(0, 2):
            ul = 1 + vertical_grid * 12 + 3 * grid
            uc = ul + 1
            ur = ul + 2
            ll = ul + 6
            lc = ul + 7
            lr = ul + 8
            #Constraints for Upper left
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lc) + "]")
            task.addConstraint("value[" + str(ul) + "] != value[" + str(lr) + "]")
            # Constraints for Upper Center
            task.addConstraint("value[" + str(uc) + "] != value[" + str(ll) + "]")
            task.addConstraint("value[" + str(uc) + "] != value[" + str(lr) + "]")
            # Constraints for Upper right
            task.addConstraint("value[" + str(ur) + "] != value[" + str(lc) + "]")
            task.addConstraint("value[" + str(ur) + "] != value[" + str(ll) + "]")


def add_set_values(task, values, size):
    for i in range(0, size):
        for j in range(0, size):
            if values[i][j] != 0:
                task.setValue(i*size + j + 1, values[i][j])


def solve_sudoku(size, path, values)->CS:
    task = create_sudoku_csp(size, path)
    add_set_values(task, values, size)
    task.testAllDefaultParams(timeout=1)
    return task


def check_uniqueness(task, size, values, algorithm):
    #print(f"Calculating first Solution for {size}x{size} Sudoku")
    algorithm_map = {
        "depth_first_search": lambda: task.solve_dfs(timeout=1),
        "BackTracking": lambda: task.solve_BackTrack(timeout=1),
        "ForwardChecking": lambda: task.solve_ForwardChecking(timeout=1),
        "ForwardChecking_MRV": lambda: task.solve_ForwardChecking_MRV(timeout=1),
        "ForwardChecking_MRV_LCV": lambda: task.solve_ForwardChecking_MRV_LCV(timeout=1),
        "HillClimbing_chooseBest": lambda: task.solve_HillClimbing_chooseBest(timeout=1),
        "HillClimbing_greedyBias": lambda: task.solve_HillClimbing_greedyBias(timeout=1),
        "HillClimbing_chooseRandom": lambda: task.solve_HillClimbing_chooseRandom(timeout=1),
        "GeneticAlgo": lambda: task.solve_GeneticAlgo(timeout=1),
        "local_beam_search": lambda: task.solve_local_beam_search(timeout=1),
        "Simulated_Annealing": lambda: task.solve_Simulated_Annealing(timeout=1),
        "ArcConsistent_BackTracking": lambda: task.solve_ArcConsistent_BackTracking(timeout=1),
        "novelAlgorithm": lambda: task.solve_novelAlgorithm(timeout=1)
    }
    first_time = 0
    if algorithm in algorithm_map:
        first_time_start = time.time()
        algorithm_map[algorithm]()
        first_time_end = time.time()
        first_time = first_time_end - first_time_start
    res = ""
    for i in range(0, size):
        for j in range(0, size):
            if i < size-1 or j < size-1:
                res += "value["+str(i*size + j + 1)+"] == "+str(task.value[i*size + j + 1])+" and "
            else:
                res += "value[" + str(i*size + j + 1) + "] == " + str(task.value[i*size + j + 1])
    unique_task = create_sudoku_csp(size, path="CheckedSolutions/")
    unique_task.addConstraint("not (" + res + ")")
    add_set_values(unique_task, values, size)
    unique_algorithm_map = {
        "depth_first_search": lambda: unique_task.solve_dfs(timeout=1),
        "BackTrack": lambda: unique_task.solve_BackTrack(timeout=1),
        "ForwardChecking": lambda: unique_task.solve_ForwardChecking(timeout=1),
        "ForwardChecking_MRV": lambda: unique_task.solve_ForwardChecking_MRV(timeout=1),
        "ForwardChecking_MRV_LCV": lambda: unique_task.solve_ForwardChecking_MRV_LCV(timeout=1),
        "HillClimbing_chooseBest": lambda: unique_task.solve_HillClimbing_chooseBest(timeout=1),
        "HillClimbing_greedyBias": lambda: unique_task.solve_HillClimbing_greedyBias(timeout=1),
        "HillClimbing_chooseRandom": lambda: unique_task.solve_HillClimbing_chooseRandom(timeout=1),
        "GeneticAlgo": lambda: unique_task.solve_GeneticAlgo(timeout=1),
        "local_beam_search": lambda: unique_task.solve_local_beam_search(timeout=1),
        "Simulated_Annealing": lambda: unique_task.solve_Simulated_Annealing(timeout=1),
        "ArcConsistent_BackTracking": lambda: unique_task.solve_ArcConsistent_BackTracking(timeout=1),
        "novelAlgorithm": lambda: unique_task.solve_novelAlgorithm(timeout=1)
    }
    #print(f"Checking uniqueness for {size}x{size} Sudoku")
    if algorithm in unique_algorithm_map:
        second_time_start = time.time()
        unique_algorithm_map[algorithm]()
        second_time_end = time.time()
        second_time = second_time_end - second_time_start
        return first_time, second_time
    '''f = open(unique_task.solution_path + 'BackTrack_Solution.txt', 'r')
    text = f.read()
    if "No valid solution exist" in text:
        print("Unique sudoku found")
    else:
        print("Sudoku not unique")
    f.close()'''
