# cook your dish here
T=int(input())
for i in range(T):
    A,B,K=map(int,input().split())
    dist=abs(A-B)
    steps=(dist+K-1)//K
    print(steps)