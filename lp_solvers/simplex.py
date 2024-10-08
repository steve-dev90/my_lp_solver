import numpy as np

from utility.utility import pivot

def simplex(lp, problem_type):
    optimal = False
    loop_num = 0
    while (not optimal) | (loop_num > 3):
        entering_row, entering_col = determine_entering_var(lp, problem_type)
        print(f'Entering variable : row = {entering_row}, col = {entering_col}')
        pivoted_lp = pivot(lp, entering_row, entering_col)
        print(pivoted_lp)
        optimal = check_optimal(lp)
        print(f'Pivoted Lp optimal: {optimal}')
        loop_num += 1

def check_optimal(lp):
    #identify the non basic variables (NBVs)
    num_basic_vars = 0
    for j in range(0, lp.shape[1]):
        #Check if variable is a non-basic variable
        print()
        if np.sum(np.abs(lp[:,j])) != 1:
            #if any NBV is negative an optimal solution has not been found
            if lp[0, j] < 0:
                return False
        else:
            num_basic_vars += 1
    #There should be m = number of rows basic variables
    if num_basic_vars < lp.shape[0]:
        print("Insufficient number of basic variables found")
        return False
    return True

def determine_entering_var(lp, problem_type):

    if problem_type == 'max':
        #Find the most negative col in first row for a maximise LP problem
        entering_col = np.argmin(lp[0])
    else:
        #Find the most positive col in the first row for a minimise LP problem
        entering_col = np.argmax(lp[0])

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