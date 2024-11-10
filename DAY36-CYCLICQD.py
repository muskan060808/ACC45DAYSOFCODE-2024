# cook your dish here
T=int(input(" "))
for i in range(T):
    A,B,C,D=map(int,input().split())
    if A+C==180 or B+D==180:
        print("yes")
    else:
        print("No")