"""
set comprehension 
given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}"""

l=[1, 2, 5, 2, 3, 1, 4, 5]

s=set(l)
s={x**2 for x in s}
print(s)