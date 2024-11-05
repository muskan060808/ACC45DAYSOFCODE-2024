# cook your dish here
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    found=False
    for j in range(0,11):
        if A+B+j==21:
            print(j)
            found=True
            break
    if not found:
        print(-1)
         