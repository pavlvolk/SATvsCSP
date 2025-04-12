import os
import re
from operator import contains

import SudokuCSP
import SudokuSAT
import ast

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


def test_sat(hints, first_times, second_times, solved):
    for sudoku in hints:
        cnf, model, first_time = SudokuSAT.solve_sudoku(len(sudoku), sudoku)
        solvable, second_time = SudokuSAT.check_uniqueness(cnf, model, len(sudoku))
        first_times.append(first_time)
        second_times.append(second_time)
        solved.append(solvable)

def test_csp(hints):
    algorithm_keys = [
        "depth_first_search",
        "BackTrack",
        "ForwardChecking",
        "ForwardChecking_MRV",
        "ForwardChecking_MRV_LCV",
        "HillClimbing_chooseBest",
        "HillClimbing_greedyBias",
        "HillClimbing_chooseRandom",
        "GeneticAlgo",
        "local_beam_search",
        "Simulated_Annealing",
        "ArcConsistent_BackTracking",
        "novelAlgorithm"
    ]
    algorithm_times = dict.fromkeys(algorithm_keys)
    for algorithm in algorithm_keys:
        algorithm_times[algorithm] = []
    for sudoku in hints:
        task = SudokuCSP.create_sudoku_csp(len(sudoku), "Solutions/")
        SudokuCSP.add_set_values(task, sudoku, len(sudoku))
        for algorithm in algorithm_keys:
            first_time, second_time = SudokuCSP.check_uniqueness(task, len(sudoku), sudoku, algorithm)
            algorithm_times.get(algorithm).append((first_time, second_time))
    return algorithm_times



def test_time(number_of_tests, path):
    with open(path, "r") as f:
        hints = []
        count = 0
        for line in f:
            if count >= number_of_tests:
                break
            hints.append(ast.literal_eval(line))
            count += 1
    first_times_sat = []
    second_times_sat = []
    solvable_sat = []
    test_sat(hints, first_times_sat, second_times_sat, solvable_sat)
    times = test_csp(hints)
    times_sat = []
    for i in range(len(first_times_sat)):
        times_sat.append((first_times_sat[i], second_times_sat[i]))
    times["SAT"] = times_sat
    average_times = dict.fromkeys(times)
    for key in times.keys():
        sum_times = 0
        for time in times[key]:
            first_time, second_time = time
            sum_times += first_time+second_time
        average_times[key] = sum_times / len(times[key])
    return times, average_times



'''
cnf4, model4 = SudokuSAT.solve_sudoku(4, hints4)
SudokuSAT.check_uniqueness(cnf4, model4, 4)
cnf6, model6 = SudokuSAT.solve_sudoku(6, hints6)
SudokuSAT.check_uniqueness(cnf6, model6, 6)
cnf9, model9 = SudokuSAT.solve_sudoku(9, hints9)
SudokuSAT.check_uniqueness(cnf9, model9, 9)

task4 = SudokuCSP.create_sudoku_csp(4, "Solutions/")
SudokuCSP.add_set_values(task4, hints4, 4)
SudokuCSP.check_uniqueness(task4, 4, hints4)
task6 = SudokuCSP.create_sudoku_csp(6, "Solutions/")
SudokuCSP.add_set_values(task6, hints6, 6)
SudokuCSP.check_uniqueness(task6, 6, hints6)
task9 = SudokuCSP.create_sudoku_csp(9, "Solutions/")
SudokuCSP.add_set_values(task9, hints9, 9)
SudokuCSP.check_uniqueness(task9, 9, hints9)
'''


#print(test_time(2, "sudoku_test_set_9x9.txt"))
#print(test_time(10, "sudoku_test_set_4x4.txt"))
print(test_time(3, "sudoku_test_set_6x6.txt"))