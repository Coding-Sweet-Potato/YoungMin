# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
def print_rangoli(size):
    result = []
    alphabet = [chr(i) for i in range(97,123)]
    
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        string = s[::-1]+s[1:]
        result.append(string.center(4*size - 3,'-'))
    
    print('\n'.join(result[:0:-1]+result))