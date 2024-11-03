# cook your dish here
N = int(input())
cumulative_score1 = 0
cumulative_score2 = 0
max_lead = 0
winner = 0
for _ in range(N):
    score1, score2 = map(int, input().split())
    cumulative_score1 += score1
    cumulative_score2 += score2
    current_lead = abs(cumulative_score1 - cumulative_score2)
    if cumulative_score1 > cumulative_score2:
        current_winner = 1
    else:
        current_winner = 2
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_winner
print(winner, max_lead)