# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
dic = {}
for _ in range(int(input())):
    s = input()
    try:
        dic[s] += 1
    except:
        dic[s] = 1
print(len(dic))
print(*dic.values())
