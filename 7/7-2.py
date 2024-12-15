from itertools import combinations_with_replacement
from itertools import combinations
from itertools import accumulate, product

def check_valid(tv, eq):
    ops_list = list(product(['+','*'], repeat=len(eq)-1))
    for ops in ops_list:
        val = eq[0]
        for v, op in zip(eq[1:],ops):
            val = eval(f'{val}{op}{v}')        
        if val == tv:
            return tv
    return 0

def new_check_valid(tv, eq):
    ops_list = list(product(['+','*','s'], repeat=len(eq)-1))
    for ops in ops_list:
        val = eq[0]
        for v, op in zip(eq[1:],ops):
            if op == 's':
                val = int(eval(f'str({val})+str({v})'))
            else:
                val = eval(f'{val}{op}{v}')
        if val == tv:
            return tv
    return 0


if __name__ == '__main__':
    with open('7.txt', 'r') as file:
        txt = file.read().splitlines()

    total = 0
    for li in txt:
        tv = int(li.split(':')[0].strip())
        eq = [int(x) for x in li.split(':')[1].strip().split(' ')]
        print(tv,eq)
        result = check_valid(tv,eq)
        if result != 0:
            total += result
            print(total)
            continue
        else:
            result = new_check_valid(tv,eq)
            if result > 0:
                total += result
                print(total)
    
    print(total)