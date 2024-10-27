# cook your dish here
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sum=0
    for i in range(n-1):
        sum=sum+abs(a[i+1]-a[i])-1
    print(sum)
    