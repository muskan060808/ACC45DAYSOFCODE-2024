# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    nibble=N%4
    if nibble==0:
        print("good")
    else:
        print("not good")