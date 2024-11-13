# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if A<=B and A<=C:
        print(B+C)
    elif B<=C and B<=A:
        print(C+A)
    elif C<=A and C<=B:
        print(A+B)