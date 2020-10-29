
def i(data):
    for j in range(1,data+1):
        yield j
s=int(input("enter number: "))
for t in i(s):
    print(t)


