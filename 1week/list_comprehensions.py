if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = []
    for i in range(x+1):
        for j in range(y+1):
            for l in range(z+1):
                if sum([i,j,l]) != n:
                    output.append([i,j,l])
    print(output)
