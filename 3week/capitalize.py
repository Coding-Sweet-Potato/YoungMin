# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
def solve(s):
    answer = ''
    for idx,i in enumerate(s):
        if idx == 0:
            if i.isalnum(): 
                answer += i.upper()
            else:
                answer += i
        elif i.isalnum() and s[idx-1] == ' ':
            answer += i.upper()
        else:
            answer += i
    return answer