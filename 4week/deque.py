# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
from collections import deque
d = deque()
for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'append':
        d.append(int(command[1]))
    if command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    if command[0] == 'pop':
        d.pop()
    if command[0] == 'popleft':
        d.popleft()
print(*d)