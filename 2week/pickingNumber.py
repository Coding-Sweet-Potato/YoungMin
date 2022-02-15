# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
import os

def pickingNumbers(a):
    
    maximum=0        
    for i in range(100):
        maximum = max(maximum, a.count(i)+a.count(i+1))                      
    
    return maximum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
