# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    j=Y*2
    if j>X:
        print(0)
    else:
        print(X//j)
    