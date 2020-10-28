#Try out read, readline(s), and looping over file object

fileobject=open("collectingArgs.py","r")
#it reads entire file
print(fileobject.read())
#it reads line by line
print(fileobject.readline())
print(fileobject.readline())

"""
output:
> python readfile.py
#Use sys module to get command line args and print them
import sys

NumberofArgs=len(sys.argv)

print("Entered arguments are:")
for i in range(0,NumberofArgs):
    print(sys.argv[i])


"""