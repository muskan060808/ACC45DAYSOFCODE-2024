# cook your dish here
X,Y=map(int,input().split())
remaining_time=X-Y
Y=Y//2
total_time=remaining_time+Y
print(total_time)
