# cook your dish here
T=int(input())
for i in range(T):
    number=int(input())
    if number>1:
        for j in range(2,int(number/2)+1):
            if number%j==0:
                print("no")
                break
        else:
            print("yes")
    else:
        print("no")