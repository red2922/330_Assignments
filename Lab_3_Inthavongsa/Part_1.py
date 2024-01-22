
def minandMax(lst,i, minN, maxN):
    if i == 0:
        if len(lst) == 0:
            return
        minN = lst[0]
        maxN = lst[0]

    if i == len(lst):
        return minN, maxN

    if lst[i] > maxN:
        maxN = lst[i]

    elif lst[i] < minN:
        minN = lst[i]

    return minandMax(lst, i + 1, minN, maxN)


def stringToListInt(string):
    int_list = []
    new_list = list(string.split(","))
    for i in new_list:
        int_list.append((i))

    return int_list





