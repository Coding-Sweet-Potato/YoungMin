if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ls = sorted(arr)
    maximum = max(ls)
    while True:
        try:
            ls.remove(maximum)
        except:
            print(ls[-1])
            break