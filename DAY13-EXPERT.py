# cook your dish here
T=int(input(" "))
for i in range(T):
    x,y=map(int,input().split())
    if 2*y>=x:
        print("yes")
    else:
        print("no")