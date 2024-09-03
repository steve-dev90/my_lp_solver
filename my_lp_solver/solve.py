import numpy as np

from lp_solvers.simplex import simplex

def main():
    lp, problem_type = get_lp()
    print(lp)
    simplex(lp, problem_type)

def get_lp():
    std_form = np.array([
        [1, -60, -30, -20, 0, 0, 0, 0, 0],
        [0,   8,   6,   1, 1, 0, 0, 0, 48],
        [0,   4,   2, 1.5, 0, 1, 0, 0, 20],
        [0,   2, 1.5, 0.5, 0, 0, 1, 0, 8],
        [0,   0,   1,   0, 0, 0, 0, 1, 5]
    ])
    std_form2 = np.array([
        [1, -2, 1, -1, 0, 0, 0, 0],
        [0,  3, 1,  1, 1, 0, 0, 60],
        [0,  2, 1,  2, 0, 1, 0, 20],
        [0,  2, 2,  1, 0, 0, 1, 20]
    ]).astype(np.float32)

    problem_type = 'max'

    std_form3 = np.array([
        [1, -2,  3, 0, 0, 0],
        [0,  1,  1, 1, 0, 4],
        [0,  1, -1, 0, 1, 6]
    ]).astype(np.float32)
    problem_type = 'min'


    return std_form3, problem_type

if __name__ == "__main__":
    main()