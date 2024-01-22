import Part_1
#make a recursive function that returns the reverse of a string

def r_string(f_string,lst):
    if len(f_string) == 0:
        return
    else:
        lst.append(f_string[-1])
        f_string = list(f_string)
        f_string.pop()
        f_string = ''.join(f_string)
        r_string(f_string,lst)
    return ''.join(lst)







