# cook your dish here
T=int(input(" "))
for i in range(T):
    N=int(input( ))
    A=list(map(int,input().split()))
    degree=0
    for i in range(N):
        if A[i]!=0:
            degree=i
    print(degree)