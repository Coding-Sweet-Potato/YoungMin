# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

A,B = map(int,input().split())
ls,ls2 = [],[]
for i in range(A+B):
    group = input()
    
    if i > A-1:
        ls2.append(group)
    else:
        ls.append(group)
for i in ls2:
    res_list = list(filter(lambda x: ls[x] == i, range(len(ls))))
    result = list(map(lambda x: str(x+1),res_list))
    answer = ' '.join(result)
    if answer == '':
        print(-1)
    else:
        print(answer)
    
        