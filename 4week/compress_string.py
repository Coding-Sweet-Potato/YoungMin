# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
from itertools import groupby
ans = [(len(list(g)),int(k)) for k, g in groupby(input())]
print(*ans)