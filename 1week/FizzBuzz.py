def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

if __name__ == '__main__':
    
    n = int(input().strip())
    for i in range(1,n+1):
        fizzBuzz(i)