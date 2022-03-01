def matmul(matrix1, matrix2):
    if len(matrix1) != 3 or len(matrix2) != 3:
        return None
    result = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result