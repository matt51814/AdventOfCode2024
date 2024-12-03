import re
if __name__ == '__main__':
    with open('3.txt', 'r') as file:
        txt = file.read()

    print(txt)
    print(re.findall('mul\([\d]*\,[\d]*\)+', txt))

    sum = 0
    for string in re.findall('mul\([\d]*\,[\d]*\)+', txt):
        string = string.replace('mul(','')
        string = string.replace(')','')
        string = string.split(',')
        n1, n2 = int(string[0]), int(string[1])
        sum += n1 * n2
    print(sum)