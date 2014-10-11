## module with data processing functions

"""
data processing function, creates separation matrix throught the dictionary created from the input file,
finds every paths then select lowest
"""

def     do_separation_matrix(data :dict, dump :bool):
    if dump:
        print("degrés de séparation (maison):")
    guys = sorted(data.keys())
    matrix = []
    index = 0
    nb = 0
    while index < len(guys):
        matrix.append([])
        sepguys = dict.fromkeys(guys, 0)
        find_em_all(data, guys, guys[index], sepguys, 0)
        sepguys[guys[index]] = 0
        for key in sorted(sepguys.keys()):
            matrix[index].append(sepguys[key])
        index += 1
    return matrix
        
"""
data processing function, used by separation algo
"""

def     find_em_all(data :dict, guys :list, index :str, sepguys :dict, count :int):
    for i in range(len(data[index])):
        if sepguys[data[index][i]] == 0 or sepguys[data[index][i]] > count:
            sepguys[data[index][i]] = count + 1
            find_em_all(data, guys, data[index][i], sepguys, count + 1)

"""
data processing function, uses separation matrix to define the best connexion path between two guys
"""

def     find_target(data, guys, index, target, matrix, count):
    for i, item in enumerate(matrix[guys.index(index)]):
        if count == 0:
            return
        elif item == 1 and matrix[i][guys.index(target)] == count - 1:
            print("{} est ami(e) avec {}".format(index, guys[i]))
            find_target(data, guys, guys[i], target, matrix, count - 1)
