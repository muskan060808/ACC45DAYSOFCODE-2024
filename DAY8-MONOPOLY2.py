# cook your dish here
T=int(input(" "))
for i in range(T):
    A,B,C,D=map(int,input().split())
    if A>B+C+D or B>A+C+D or C>A+B+D or D>A+B+C:
        print("yes")
    else:
        print("no")