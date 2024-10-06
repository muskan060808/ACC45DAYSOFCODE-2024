# cook your dish here
T=int(input(" "))
for i in range(T):
    X,Y=map(int,input().split())
    M=(Y-1)//X
    print(M)