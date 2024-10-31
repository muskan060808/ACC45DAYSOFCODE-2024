# cook your dish here
T=int(input())
for i in range(T):
    P,Q=map(int,input().split())
    serves=(P+Q)//2
    if serves%2==0:
        print("Alice")
    else:
        print("Bob")