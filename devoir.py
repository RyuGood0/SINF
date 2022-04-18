def multiply(A,B):
    # Vérifie que les deux matrices sont de bonnes dimensions
    if type(A[0]) != list or type(B[0]) != list: raise Exception('Dimension mismatch')
    if len(A[0]) != len(B): raise Exception('Dimension mismatch')

    # Initialise la matrice résultat
    m = len(A)
    n = len(B[0])
    out = [[0]*n for i in range(m)]

    # Multiplie les matrices
    for i in range(m):
        for j in range(n):
            for k in range(len(B)):
                out[i][j] += A[i][k] * B[k][j]

    return out