#Use sys module to get command line args and print them
import sys

NumberofArgs=len(sys.argv)

print("Entered arguments are:")
for i in range(0,NumberofArgs):
    print(sys.argv[i])

""" Output
> python collectingargs.py 1 2 "tarun" [2,4,"arun"]
Entered arguments are:
collectingargs.py
1
2
tarun
[2,4,arun
]"""