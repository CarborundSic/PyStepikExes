def is_isolate(matrix, x, y):  # проверить на изолированность единички
    n = len(matrix)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if (i or j) and matrix[x+i][y+j]:
                    return False
    return True


def verify(matrix):  # искать единичку в матрице из нулей
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 and not is_isolate(matrix, i, j):
                return False
    return True
