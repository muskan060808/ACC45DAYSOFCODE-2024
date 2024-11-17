# cook your dish here
from math import ceil
T=int(input())
for i in range(T):
    X,Y,R=map(int,input().split())
    extra_sticks=R//30
    total_sticks=X+extra_sticks
    max_plates=ceil(total_sticks/Y)
    print(max_plates)