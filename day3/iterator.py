class I:
    def __init__(self,num):
        self.num=num
        self.data=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.data== self.num:
            raise StopIteration
        self.data=self.data+1
        return self.data
s=int(input("enter number: "))
enq=I(s)
iter(enq)

for t in enq:
    print(t)


