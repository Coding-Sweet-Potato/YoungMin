# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    div = len(string)//k
    for i in range(1,div+1):   
        result = string[k * (i-1) : k * i]
        tmp = dict.fromkeys(list(result))
        print(''.join(list(tmp)))
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)