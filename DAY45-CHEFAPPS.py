# cook your dish here
T=int(input())
for i in range(T):
    S,X,Y,Z=map(int,input().split())
    free_memory = S - (X + Y)

    if free_memory >= Z:
        print(0)
    elif free_memory + max(X, Y) >= Z:
        print(1)
    else:
        print(2)
        