# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter
X = int(input())
size_ls = list(map(int,input().split()))
shoes = Counter(size_ls)
N = int(input())
result = 0
for i in range(N):
    size,price = map(int,input().split())
    if shoes[size]:
        result += price
        shoes[size] -= 1
print(result)
