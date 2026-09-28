def gaussian_elimination(A, b, eps=10**-6):
    nrows = len(A)
    nvars = len(A[0])

    A = [
        A[i] + [b[i]] for i in range(nrows)
    ]

    pivot_cols = []
    free_cols = []

    # Eliminate
    for var in range(nvars):
        n_pivots = len(pivot_cols)

        nonzero_row = None
        for row in range(n_pivots, nrows):
            if abs(A[row][var]) > eps:
                nonzero_row = row
                break

        if nonzero_row == None:
            free_cols.append(var)
            continue

        if nonzero_row != n_pivots:
            for i in range(nvars+1):
                A[n_pivots][i], A[nonzero_row][i] = A[nonzero_row][i], A[n_pivots][i]
            nonzero_row = n_pivots

        for row in range(nrows):
            if row == nonzero_row:
                continue

            factor = A[row][var] / A[nonzero_row][var]

            for i in range(nvars+1):
                A[row][i] += A[nonzero_row][i] * -factor

        pivot_cols.append(var)


    # Check whether the system is consistent
    for row in range(nrows):
        allzero = True
        for var in range(nvars):
            if abs(A[row][var]) > eps:
                allzero = False
                break

        if allzero and abs(A[row][nvars]) > eps:
            return None
    

    # Normalize
    for row, pivot in enumerate(pivot_cols):
        pivot_val = A[row][pivot]
        for col in range(nvars+1):
            A[row][col] /= pivot_val

    # # Particular solution
    # particular = [0.0]*nvars
    # for row, pivot in enumerate(pivot_cols):
    #     particular[pivot] = A[row][nvars]


    # # Null space solution
    # free_vecs = []
    # for free_var in free_cols:
    #     free = [0.0]*nvars
    #     free[free_var] = 1
    
    #     for row in range(nrows):
    #         free[row] = -A[row][free_var] 

    #     free_vecs.append(free)

    particular = [0.0]*nvars
    free_vars = [[0.0]*nvars for i in range(len(free_cols))]
    for row, pivot in enumerate(pivot_cols):
        particular[pivot] = A[row][nvars]

        for idx, free_col in enumerate(free_cols):
            free_vars[idx][pivot] = -A[row][free_col]

    for idx, free_col in enumerate(free_cols):
        free_vars[idx][free_col] = 1

    # 2 -x + y = 0
    # -x + y = 2
    # y = 2+x
    # 5-y = 0
    # y = 5
    # x = y-2
    # 2 - x + y | BUDE VZDY RIESENIE pre 1. suradnicu = 1. jolt
    # 11 - x + y


    print('----')
    for x in A:
        print(x)

    print('----')
    
    return particular, free_vars

if __name__ == '__main__':

    # for x in gaussian_elimination(
    #     [
    #         [1,1,-1],
    #         [2,-1,1],
    #         [1,2,2]
    #     ],
    #     [-2, 5, 1]
    # ):
    #     print(x)

    # for x in gaussian_elimination(
    #     [
    #         [1,2,-1],
    #         [2,4,-2],
    #     ],
    #     [3, 6]
    # ):
    #     print(x)

    for x in gaussian_elimination(
        [
            [1,2,-1, 1, 3],
            [2,4,-2,3,7],
            [1,2,-1,2,4],
            [3,6,-3,5,11]
        ],
        [4,10,6,16]
    ):
        print(x)
    
        
        
        