"""dictionaries 
given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension"""

nums=[1,2,3]

s={}
s={x+1:(x+1)**2 for x in range(0,len(nums))}
print(s)
l=[s[x] for x in s]
print(l)

"""output:
{1: 1, 2: 4, 3: 9}
[1, 4, 9]
"""