# cook your dish here
T=int(input(" "))
for i in range(T):
    B1,B2,B3=map(int,input().split())
    if B1+B2+B3<=1:
        print(" water filling time")
    else:
        print("not now")