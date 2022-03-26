# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
def utopianTree(n):
    height = [1]
    for i in range(1,61):
        if i % 2 ==0:
            new = height[i-1] +1
        else:
            new = height[i-1]*2
        height.append(new)
    return height[n]
