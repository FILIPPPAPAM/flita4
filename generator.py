
def create_mirror_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    with open('matrix.txt', 'w') as file:
        for i in range(0, n-1):
            matrix[i][i+1] = 1
            matrix[i+1][i] = 1
            file.write(' '.join(str(elem) for elem in matrix[i]))
            file.write(' \n')
        file.write(' '.join(str(elem) for elem in matrix[n-1]))
        file.write(' \n')

    return matrix

