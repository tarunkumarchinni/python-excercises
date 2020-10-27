List=[1,3,3,4,5,6]

List=[(List[i]**2) if (List[i]%2)!=0 else List[i] for i in range(0,len(List))]

print(List)