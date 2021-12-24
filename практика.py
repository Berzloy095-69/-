

#задача 1

n = int(input ())
def number (n):
	if n in (1, 2):
		return 1
	return  number(n - 1) + number (n - 2)

print (number(n))




#задача 2


def fib(n):
    if n <=2:
        return 1
    else:
        prev = 0
        next = 1
        for i in range (0,n):
            temp = next
            next = prev + next
            prev = temp
            i = i + 1
        return prev



задача 3 

numb = [0, 1]
def fib(n):
	y = 0
	z = 1
	for i in range (0,n - 1):
		x = numb[y] + numb [z]
		y = y + 1
		z = z + 1
		numb.append(x)
	return numb
result = fib(int(input()))
print (result)




задача 4


import math
def fib(n):
	x = ((1 + math.sqrt(5)) / 2) ** n
	y = ((1 - math.sqrt(5)) / 2) ** n
	z = (x - y) / math.sqrt(5)
	return z
result = fib(int(input()))
print ( round (result))




задача 5 

n = int(input())
d = n / 3
f = n // 3
T = "even"
F = "odd"
def fib_eo(n):
	if f < d:
		return T
	else: 
		return F			
print (fib_eo(n))



задача 6 

from collections import Counter
import sys

class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')
    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return  [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]
    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res

def huffman(my_string):
    
    unic = []
    unique_numbers = set(my_string)
    
    for my_string in unique_numbers:
        unic.append(my_string)
    
    return len(unic)

my_string = "Errare humanum est."
tree = get_tree(my_string)
codes = get_code(tree)
coding_str = coding(my_string, codes)
decoding_str = decoding(coding_str, codes)

print(huffman(my_string),sys.getsizeof(my_string)) 

print(codes)

print('Сжатая строка: ', coding_str)

print('Исходная строка: ', decoding_str)
