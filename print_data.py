## module with print functions for some eyegasm

"""
print function, shows all the guys involved in alpha sorted order
"""

def     dump_guys(data :dict):
    print("personnes concernées :")
    for key in sorted(data.keys()):
        print('\t' + str(key))

"""
print function, prints a matrix
"""

def     dump_matrix(matrix):
    for line in matrix:
        print("\t", end='')
        for item in line:
            print("  {}".format(item), end='')
        print("\n", end='')
