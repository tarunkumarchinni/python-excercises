#Create a list of lists using nested list comprehension.
List=[[1,2,3],[4,5,6],[7,8,9,10],[11,12,"raj"]]

list=[[i[x] for i in List] for x in range(0,len(List)-1)]

print(List)
