import numpy as np

from utility.utility import pivot

def simplex(lp, problem_type):
    optimal = False
    loop_num = 0
    lp_loop = lp
    while (not optimal) & (loop_num < 3):
        entering_row, entering_col = determine_entering_var(lp_loop, problem_type)
        print(f'Entering variable : row = {entering_row}, col = {entering_col}')
        pivoted_lp = pivot(lp, entering_row, entering_col)
        print(pivoted_lp)
        optimal = check_optimal(pivoted_lp, problem_type)
        print(f'Pivoted Lp optimal: {optimal}')
        lp_loop = pivoted_lp
        loop_num += 1
    return lp_loop

def check_optimal(lp, problem_type):
    #identify the non basic variables (NBVs)
    num_basic_vars = 0
    num_top_row_zero_coeffs = 0
    for j in range(0, lp.shape[1]):
        #Check if variable is a non-basic variable
        if np.sum(np.abs(lp[:, j])) != 1:
            # Check for negative NBV in maximization problems
            if problem_type == 'max' and lp[0, j] < 0:
                return False

            # Check for positive NBV in minimization problems
            if problem_type == 'min' and lp[0, j] > 0:
                return False

            # Check for LPs with alternative solutions
            if lp[0, j] == 0:
                num_top_row_zero_coeffs += 1
        else:
            # Increment the number of basic variables
            num_basic_vars += 1

    #There should be m = number of rows basic variables
    if num_basic_vars < lp.shape[0]:
        print("Insufficient number of basic variables found")
        return False

    if num_top_row_zero_coeffs > 0:
        print("There may be alternative solutions to the LP")

    return True

def determine_entering_var(lp, problem_type):

    if problem_type == 'max':
        #Find the most negative col in first row for a maximise LP problem
        entering_col = np.argmin(lp[0])
    else:
        #Find the most positive col in the first row for a minimise LP problem
        entering_col = np.argmax(lp[0])

    #Check if solution is unbounded
    if all(lp[1:, entering_col]< 0):
        raise Exception("All rows in ratio test have a negative number - unbounded LP")

    #find the lowest ratio rhs/col coeff
    lowest_ratio = np.max(lp[:,-1])
    entering_row = 0
    for i in range(1, lp.shape[0]):
        row_value = lp[i, entering_col]
        #test if > 0
        if row_value > 0:
            row_ratio = lp[i, -1] / row_value
            if lowest_ratio > row_ratio:
                lowest_ratio = row_ratio
                entering_row = i

    return entering_row, entering_col