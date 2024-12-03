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
    with open('3.txt', 'r') as file:
        txt = file.read()

    sum = 0

    do_dont_list = []
    # split on donts
    dont_list = txt.split(r"don't()")
    do_dont_list.append(dont_list[0])
    # for remaining
    for i in dont_list[1:]:
        # if do() isn't in the dont() - dont() list then move to next one
        if 'do()' not in i:
            continue
        # if do is in dont() - dont() list then split on first do() and take to the right of it
        do_dont_list.append(i.split(r'do()',1)[-1])

    for val in do_dont_list:
        print(val, '\n')
        sum+=sum_list_part(val)

    print(sum)
