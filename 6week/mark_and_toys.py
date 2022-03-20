# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true
def maximumToys(prices, k):
    maximum = 0
    cnt = 0
    ls = sorted(prices)
    for i in ls:
        if maximum + i <= k:
            cnt += 1
            maximum += i
    return cnt
