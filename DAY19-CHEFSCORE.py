# cook your dish here
T=int(input( ))
for i in range(T):
    N,X,Y=map(int,input().split())
    if Y%X==0:
        if Y/X <=N:
            print("yes")
        else:
            print("no")
    else:
        print("no")