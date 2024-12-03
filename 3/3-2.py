import re

def sum_list_part(li: list) -> int:
    sum = 0
    for string in re.findall(r'mul\([\d]*\,[\d]*\)+', li):
        string = string.replace('mul(','')
        string = string.replace(')','')
        string = string.split(',')
        n1, n2 = int(string[0]), int(string[1])
        sum += n1 * n2
    return sum

if __name__ == '__main__':
    with open('3-ex.txt', 'r') as file:
        txt = file.read()

    sum = 0

    do_dont_list = []
    dont_list = txt.split(r"don't()")
    for i in dont_list:
        do_dont_list.extend(i.split(r'do()',1))

    for i in do_dont_list:
        print(i,'\n')

    for idx, val in enumerate(do_dont_list):
        if idx % 2 == 0:
            sum+=sum_list_part(val)

    print(sum)
