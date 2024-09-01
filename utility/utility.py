def pivot(lp, pivot_row, pivot_col):
    pivot_row_factor = 1 / lp[pivot_row][pivot_col]
    lp[pivot_row] *= pivot_row_factor

    for i in range(lp.shape[0]):
        if i != pivot_row:
            lp[i]+= lp[pivot_row] * -lp[i][pivot_col]

    return lp