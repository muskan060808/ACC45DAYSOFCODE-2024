# cook your dish here
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    A = list(map(int, input().split()))
    max_distance = 0
    for Ai in A:
        distance = max(Ai - 1, M - Ai)
        max_distance += distance
    print(max_distance)