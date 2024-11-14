# cook your dish here
T=int(input())
for i in range(T):
    N,X,P=map(int,input().split())
    correct_marks=X*3
    incorrect_marks=(N-X)*-1
    total_marks=correct_marks+incorrect_marks
    if total_marks>=P:
        print("pass")
    else:
        print("fail")