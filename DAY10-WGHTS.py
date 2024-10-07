# cook your dish here
T=int(input(" "))
for i in range(T):
    W,X,Y,Z=map(int,input().split())
    if W==X or W==Y or W==Z or W==X+Y or W==Y+Z or W==X+Z or W==X+Y+Z:
        print("yes")
    else:
        print("no")