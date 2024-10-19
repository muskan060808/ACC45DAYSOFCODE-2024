# cook your dish here
T=int(input( ))
for i in range(T):
    x,y=map(int,input().split())
    if x<y:
        print("bike")
    elif y<x:
        print("car")
    elif x==y:
        print("same")