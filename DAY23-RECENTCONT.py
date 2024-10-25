# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    contest_codes = input().split()
    start_count = contest_codes.count('START38')
    ltime_count = contest_codes.count('LTIME108')
    print(start_count, ltime_count)