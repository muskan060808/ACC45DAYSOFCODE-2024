# cook your dish here
T=int(input(  ))
for i in range(T):
    N,K,M=map(int,input().split())
    max_candies=K*M
    if N<=max_candies:
        print(1)
    else:
        if N%max_candies==0:
            print(N//max_candies)
        else:
            print(N//max_candies + 1)