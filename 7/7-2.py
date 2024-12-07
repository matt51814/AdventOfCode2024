from itertools import combinations_with_replacement
from itertools import combinations
from itertools import product

def check_valid(li):
    tv = int(li.split(':')[0].strip())
    eq = [int(x) for x in li.split(':')[1].strip().split(' ')]
    ops_list = list(product(['+','*'], repeat=len(eq)-1))
    for ops in ops_list:
        val = eq[0]
        print(ops)
        for v, op in zip(eq[1:],ops):
            val = eval(f'{val}{op}{v}')
        print(val)
        if val == tv:
            return tv
    return 0

def sum_string(list_of_string):
    tmp = ""
    for i in list_of_string:
        tmp += i
    return tmp

if __name__ == '__main__':
    with open('7-ex.txt', 'r') as file:
        txt = file.read().splitlines()


    # result = sum([check_valid(x) for x in txt])
    # print(result)
    
    # make concat eqs and tvs
    for li in txt:
        tv = int(li.split(':')[0].strip())
        eq = li.split(':')[1].strip().split(' ')
        print(eq)
        temp_li = []
        tmp = ""
        for i in range(len(eq)-1):
            for j in range(i+1,len(eq)):
                temp_li.append(eq[i:j+1])
        print(temp_li)

        pot_list = []
        for potential_concat in temp_li:
            tmp_eq = eq.copy()
            for i in eq:
                insert_pos = tmp_eq.index(potential_concat[0])
                for val in potential_concat:
                    tmp_eq.remove(val)
                tmp_eq.insert(insert_pos, sum_string(potential_concat))
            print(tmp_eq)
            break
        # for i in temp_li:
        #     print(i)
        #     for j in eq:
        #         if j in i:
        #             pass
        #         temp_li.append(j)
        # print(temp_li)



    # li = txt[-1]
    # tv = int(li.split(':')[0].strip())
    # eq = [int(x) for x in li.split(':')[1].strip().split(' ')]
    # print(eq)
    # print(list(product(eq,repeat=2)))

    # for i, j in combinations(range(len(eq) + 1), 2):
    #     print(eq[i:j])
    #     if len(eq[i:j]) == 1:

# line = txt[-1]
# tv = int(line.split(':')[0].strip())
# eq = [int(x) for x in line.split(':')[1].strip().split(' ')]
# print(eq)

# ops_list = list(product(['+','*'], repeat=len(eq)-1))
# # ops_list = list(permutations(['*','+'], 2))
# print(ops_list)
# for ops in ops_list:
#     val = eq[0]
#     print(ops)
#     for v, op in zip(eq[1:],ops):
#         val = eval(f'{val}{op}{v}')

#     print(val)
