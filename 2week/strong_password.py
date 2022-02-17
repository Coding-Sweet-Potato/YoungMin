# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def minimumNumber(n, password):
    punc = "!@#$%^&*()-+"
    ls = [False]*4
    for i in password:
        if i.isdigit():
            ls[0] = True
        if i.islower():
            ls[1] = True 
        if i.isupper():
            ls[2] = True
        if i in punc:
            ls[3] = True
    result = 0
    if ls.count(False)>=1: 
        result += 4-sum(ls)
    if n + result < 6:
        result += (6-(n+result))
    return result
