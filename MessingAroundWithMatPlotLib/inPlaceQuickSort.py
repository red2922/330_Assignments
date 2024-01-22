def inplace_quick_sort(S, a, b):
    #s is the list/a_ray
    #a is where to begin sorting ot the right of
    #a must == 0 inorder to sort the whole list. Otherwise it will only sort the right of the index position
    #b is the element to pivot from
    #a and b must be the index. Not the value store in that specific position
    if a >= b: return
    pivot = S[b]
    left = a
    right = b -1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

        S[left], S[b] = S[b], S[left]
        inplace_quick_sort(S, a, left - 1)
        inplace_quick_sort(S, left + 1, b)


test_1 = [3,4,6,2,40,34,65,73]
test_2 = [3,4,6,2,40,34,65,73]
test_3 = [3,4,6,2,40,34,65,73]
test_4 = [3,4,6,2,40,34,65,73]

inplace_quick_sort(test_1,0,7)
inplace_quick_sort(test_2,1,7)
inplace_quick_sort(test_3,2,7)
inplace_quick_sort(test_4,3,7)

print(test_1)
print(test_2)
print(test_3)
print(test_4)

test_5 = [{'A':5}]
print(test_5[0]['A'])