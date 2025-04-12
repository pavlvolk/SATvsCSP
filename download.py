import kagglehub
import numpy as np

def download():
    path = kagglehub.dataset_download("bryanpark/sudoku")

    print("Path to dataset files:", path)


def extract_data_9x9():
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


def extract_data_4x4():
    quizzes = np.zeros((1000000, 16), np.int32)
    solutions = np.zeros((1000000, 16), np.int32)
    for i, line in enumerate(open('4x4_sudoku_unique_puzzles.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 4, 4))
    solutions = solutions.reshape((-1, 4, 4))
    return np.array(quizzes).tolist(), np.array(solutions).tolist()


def extract_data_6x6():
    quizzes = np.zeros((50, 36), np.int32)
    solutions = np.zeros((50, 36), np.int32)
    for i, line in enumerate(open('sudoku_6x6_dataset.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 6, 6))
    solutions = solutions.reshape((-1, 6, 6))
    return np.array(quizzes).tolist(), np.array(solutions).tolist()

def write_as_list(quizzes, path):
    with open(path, "w") as f:
        for quiz in quizzes:
            f.write(str(quiz) + "\n")
        f.close()


quizzes, solutions = extract_data_6x6()
write_as_list(quizzes, "sudoku_test_set_6x6.txt")

