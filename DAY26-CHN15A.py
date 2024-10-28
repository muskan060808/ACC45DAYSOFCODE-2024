# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    initial_characteristic=list(map(int,input().split()))
    wolverine_like_count=0
    for j in initial_characteristic:
        if (j+K)%7==0:
            wolverine_like_count+=1
    print(wolverine_like_count)