# cook your dish here
T=int(input(" "))
for i in range(T):
    n,x=map(int,input().split())
    if (n-x)<x:
        print(n-x)
    else:
        print(x)