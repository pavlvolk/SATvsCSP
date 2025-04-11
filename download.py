import kagglehub
import numpy as np

def download():
    path = kagglehub.dataset_download("bryanpark/sudoku")

    print("Path to dataset files:", path)


def extract_data():
    quizzes = np.zeros((1000000, 81), np.int32)
    solutions = np.zeros((1000000, 81), np.int32)
    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))
    return np.array(quizzes).tolist(), np.array(solutions).tolist()


def write_as_list(quizzes):
    with open("sudoku_test_set.txt", "w") as f:
        for quiz in quizzes:
            f.write(str(quiz) + "\n")
        f.close()


quizzes, solutions = extract_data()
write_as_list(quizzes)

