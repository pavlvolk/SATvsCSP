Simple python code to compare CSP- and SAT-Solvers with different amounts of 4x4, 6x6 and 9x9 sudokus.
The sudokus should be given as a csv or or as lists in a txt. 
  - If they are in csv they first need to be converted using the download file provided.
  - If they are in a double list format the can just be processed by the main file.

Usage:
  You use the method "test_time" with the amount of sudokus you want to test and the path to the .txt file.
  The method will return the list of the needed times in the console.
  The returned times are structured as follows:
    1. The name of the algorithm as the key of the list.
    2. A list with of tuples structured as (first_time, second_time) referencing the first time the sudoku was solved and the second time the algorithm tried to solve it to make sure there is a unique solution.
    3. Then there is another list again containing the name of the algorithm and the average time needed for each algorithm to solve the sudoku.
