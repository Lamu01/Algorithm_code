# 계단 오르기
n = int(input())
score = [int(input()) for i in range(n)]
d = [0]*(n)

d[0] = score[0]
d[1] = score[0] + score[1]
for i in range(2,n):
    d[i] = max(d[i-3]+score[i-1]+score[i],
    d[i-2]+score[i])
print(d[-1])