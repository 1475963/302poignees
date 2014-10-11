## module with file parsing functions to extract and threat some data

sep1 = " est ami avec "
sep2 = " est amie avec "

"""
file parsing function, extracts data from input file into a dictionary
"""

def     extract_data(filename :str) -> dict:
    data = dict()
    print("File used : " + filename + "\n")
    fileStream = open(filename, 'r')
    for line in fileStream:
        if is_valid_entry(line):
            line = line.rstrip()
            left = get_left_name(line)
            right = get_right_name(line)
            if data.get(left) == None:
                data[left] = list()
            data[left].append(right)
            if data.get(right) == None:
                data[right] = list()
            data[right].append(left)
    return data

"""
file parsing function, check is the separator between two guys exists
"""

def     is_valid_entry(line :str) -> bool:
    if line.count(sep1) == 1 or line.count(sep2):
        return True
    return False

"""
file parsing function, return the name of left guy in the sentence
"""

def     get_left_name(line :str) -> str:
    if line.find(sep1) == -1:
        index = line.find(sep2)
    else:
        index = line.find(sep1)
    return line[0:index]

"""
file parsing function, return the name of right guy in the sentence
"""

def     get_right_name(line :str) -> str:
    if line.find(sep1) == -1:
        index = line.find(sep2)
        return line[index + len(sep2):]
    else:
        index = line.find(sep1)
        return line[index + len(sep1):]
