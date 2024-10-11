# cook your dish here
T=int(input(" "))
for i in range(T):
    a,b,c,d=map(int,input().split())
    max_tastiness=max(a,b)+max(c,d)
    print(max_tastiness)