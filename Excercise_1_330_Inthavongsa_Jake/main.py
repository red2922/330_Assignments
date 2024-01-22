
#A
def is_multiple(n,m):
    r = m % n
    if r == 0:
        return True
    else:
        return False

print(is_multiple(5,20))
print(is_multiple(6,98))

#B
def minmax(data):
    nums_sorted = sorted(data)
    min_num = nums_sorted[0]
    max_num = nums_sorted[-1]

    return (min_num,max_num)


print(minmax([10,20,60,40,70]))
print(minmax([14,35,342,736,100,355]))
print(minmax((45,654,234,76,24,24,1,65,4)))

#C
def sumofSquares(n):
    sum = 0
    for i in range(n):
        sum += (i) ** 2

    return sum

print(sumofSquares(4))
print(sumofSquares(5))
print(sumofSquares(6))

#D # of Vowels in a string
def numVowels(string):
    string = str(string).lower()
    v_count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')

    for i in vowels:
        v_count += string.count(i)

    print("The number of vowels is " + str(v_count))

numVowels('asdfivqernvaklhuasfmeqbt')
numVowels('icadfhajhivukjnqwetboaicvubkjadbguyvbklqbwekrbga')

#E
def removePunct(sentence):
    new_sen = sentence
    punct = ('.', '?', '!', ',', ';', ':', '-', '(', ')', '[', ']', '\'', '{', '}')

    for i in punct:
        new_sen = new_sen.replace(i,'')

    return new_sen

print(removePunct('This is goi.][ng! great ! . . .  .\''))
print(removePunct('hi! Everyone. This is [] good,.. punctuation'))

