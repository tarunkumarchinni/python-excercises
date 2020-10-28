
"""myfunction is accepts the numberof argumenyts and keywords given"""
def myfunction(name,*args,**key):
    print("Welcome ",name)
    print("Entered arguments are: ")
    for i in args:  #represtents arguments
        print(i)
    print("Entered keywords are: ")
    for j in key:   #represents keywords
        print(j,":",key[j])

#single paramenter
myfunction("arun")
#with number of arguments and keywoerds calling
myfunction("arun",1,[23,3,4],20,college="MVGR",department="CSE")
    