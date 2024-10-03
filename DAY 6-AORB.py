# cook your dish here
T=int(input(" "))
for i in range(T):
    X,Y=map(int,input().split())
    ABscore=(500-X*2)+(1000-(X+Y)*4)
    BAscore=(1000-Y*4)+(500-(X+Y)*2)
    print(max(ABscore,BAscore))
    