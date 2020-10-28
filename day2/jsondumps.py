#try json.dump and load for different data structures in python

import json

fileobject=open("simple.txt","r")

x=json.load(fileobject)
#json.dump(x,fileobject)
print(x)

print(json.dumps([2,3,4]))

