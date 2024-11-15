# cook your dish here
T=int(input( ))
for i in range(T):
    N,A,B=map(int,input().split())
    odd_episode=(N+1)//2
    even_episode=N//2
    total_duration=odd_episode*B+even_episode*A 
    print(total_duration)
    