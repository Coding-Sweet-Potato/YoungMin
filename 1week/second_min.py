if __name__ == '__main__':
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([score,name])
    mini = min(ls)[0]
    ls2 = ls.copy()
    for i in ls2:
        if i[0] == mini:
            ls.remove(i)
    final = min(ls)[0]
    ls.sort(key=lambda x: x[1])
    for j in ls:
        if j[0] == final:
            print(j[1])