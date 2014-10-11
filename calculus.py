## module with calculus on matrices Cours302FTW

"""
calc function, computes the result of matrix product a * b at the index [y][x]
example :
A = [ [1, 0], [-1, 3] ]
B = [ [3, 1], [2, 1] ]

C = A * B
C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
C[0][0] = 1 * 3 + 0 * 2
"""
        
def     get_nb_matrix(a, b, y, x):
    nb = 0
    for i in range(len(a)):
        nb += a[y][i] * b[i][x]
    return nb

"""
calc function, calls get_nb_matrix for every x in every y of matrix b
"""

def     mult_matrix(a, b):
    tmp = []
    for y, line in enumerate(b):
        tmp.append([])
        for x, item in enumerate(line):
            tmp[y].append(get_nb_matrix(a, b, y, x))
            
    return tmp

"""
data processing function, creates adjacent matrix throught the dictionary created from the input file
"""

def     do_adja_matrix(data :dict, dump :bool):
    if dump:
        print("matrice d'adjacence :")
    guys = sorted(data.keys())
    matrix = []
    index = 0
    while index < len(guys):
        i = 0
        matrix.append([])
        while i < len(guys):
            j = 0
            nb = 0
            while j < len(data[guys[index]]):
                if data[guys[index]][j] == guys[i]:
                    nb = 1
                j += 1
            matrix[index].append(nb)
            i += 1
        index += 1
    return matrix

"""
calc function, G², G * G
"""

def     do_square_matrix(matrix, dump :bool):
    if dump:
        print("matrice G2 :")
    return mult_matrix(matrix, matrix)

"""
calc function, G^3, G² * G
"""

def     do_cube_matrix(a, b, dump :bool):
    if dump:
        print("matrice G3 :")
    return mult_matrix(a, b)

"""
calc function, computes separation matrix from adjacent matrix,
creates a matrix with infinite numbers then seek for lowest distances from adjacent matrix sommets
"""

def     floyd_warshall_method(matrix, dump :bool):
    if dump:
        print("degrés de séparation (warshall):")
    tmp = []
    
    for y, line in enumerate(matrix):
        tmp.append([])
        for x, item in enumerate(line):
            tmp[y].append(float("inf"))
            if matrix[y][x] > 0:
                tmp[y][x] = 1
        tmp[y][y] = 0

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp[i][j] = min(tmp[i][j], tmp[i][k] + tmp[k][j])

    return tmp
