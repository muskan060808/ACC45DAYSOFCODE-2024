# cook your dish here
T=int(input( ))
for i in range(T):
    H,X,Y=map(int,input().split())
    health_remaining=H-Y
    if health_remaining<=0:
        print(1)
    else:
        normal_attack=(health_remaining+X-1)//X
        print(1+normal_attack)