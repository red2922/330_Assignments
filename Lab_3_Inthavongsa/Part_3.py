#Put all even values before the odd values

def evenOdd(lst, i= 0, even = [], odd = []):
    if (len(even) + len(odd)) > 1 and i == 0:
        even.clear()
        odd.clear()

    if i == len(lst):
        return even,odd

    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

    return evenOdd(lst,i + 1, even, odd)









