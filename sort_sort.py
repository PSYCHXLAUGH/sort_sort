from ast import arg
from sys import argv

DATA_1 = list(map(int, list(argv[1])))
DATA_2 = list(map(int, list(argv[2])))
SORT_DATA = []
i = 0
j = 0

while len(DATA_1) + len(DATA_2) != len(SORT_DATA) and i != len(DATA_1) and j != len(DATA_2):
    if DATA_1[i] > DATA_2[j]:
        SORT_DATA.append(DATA_2[j])
        j += 1
    elif DATA_1[i] < DATA_2[j]:
        SORT_DATA.append(DATA_1[i])
        i += 1
    elif DATA_1[i] == DATA_2[j]:
        if i > j:
            SORT_DATA.append(DATA_2[j])
            j += 1
        else:
            SORT_DATA.append(DATA_2[i])
            i +=  1
    

print(SORT_DATA)
