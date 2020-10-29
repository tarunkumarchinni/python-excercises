list=[("Guido",2000,500),("Raymond",-52,1000),("jack",900,1000),("Brandon",2000,0)]
#print(list)

#dict of those with proper balances(above or equal min bal)
d={x[0]:x[1] for x in list if x[1]>x[2]}
print (d)
#{'Guido': 2000, 'Brandon': 2000}

#set of all balances
s={x[1] for x in list}
print(s)

#list of account holders
l=[x[0] for x in list]
print(l)

#dict of user and money each need to fulfill the min balance requirement (those who already have enough  bal should not be in the dict)
m={x[0]:x[2]-x[1] for x in list if x[1]<x[2]}
print(m)

#list of tuples with name and current balance if the balance is above 0
n=[x[0:2] for x in list if x[1]>0]
print(n)
