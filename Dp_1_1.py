n = int(input())
arr = list(map(int,input().split()))
# d[i]는 i번쨰 창고까지 선택했을때 최댓

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])
for i in range(2, n):
    d[i] = max(d[i-2]+arr[i], d[i-1])
print(d[n-1])