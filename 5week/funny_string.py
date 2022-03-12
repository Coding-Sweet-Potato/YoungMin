# https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true
def funnyString(s):
    ord_s = list(map(lambda x: ord(x),s))
    rev_ord_s = list(map(lambda x: ord(x),s[::-1]))
    for i in range(len(ord_s)):
        if i == len(ord_s)-1:
            break
        if abs(ord_s[i+1] - ord_s[i]) != abs(rev_ord_s[i+1] - rev_ord_s[i]):
            return "Not Funny"
    return "Funny"