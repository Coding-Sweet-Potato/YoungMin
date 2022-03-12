# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true/
def divisibleSumPairs(n, k, ar):
    answer = 0
    for i in range(n):
        for j in range(i,n):
            if (ar[i] + ar[j]) %k ==0 and i<j:
                answer += 1
    return answer