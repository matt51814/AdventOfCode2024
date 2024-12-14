import re
from itertools import combinations_with_replacement
from collections import Counter
from math import gcd

import numpy as np

# Solution
def solution(A,b):
    if np.linalg.det(A) !=0:
        inv = np.linalg.inv(A)
        sol = inv@b
        return sol
    else:
        return 'infinite solution'
     


if __name__ == "__main__":
    with open('13-ex.txt', 'r') as file:
        txt = file.read().splitlines()
    a_list =[]
    b_list =[]
    prize_list =[]
    for i in txt:
        numbers = re.findall(r"\d+", i)
        if 'Button A' in i:
            a_list.append([int(x) for x in numbers])
            continue
        if 'Button B' in i:
            b_list.append([int(x) for x in numbers])
            continue
        if 'Prize' in i:
            prize_list.append([10000000000000+int(x) for x in numbers])

    total = 0
    for a,b,prize in zip(a_list,b_list,prize_list):
          print(a)

          A = np.array([
               [a[0],b[0]],
               [a[1],b[1]]
               ])
          b = np.array(prize)
          print(A,b)
          print(np.linalg.det(A))

          x = np.linalg.solve(A,b)
          print(b/x)
          # print(np.allclose(np.dot(A, x), b))


          # print(a,b,prize)
          # print(all([is_possible(a[i],b[i],prize[i]) for i in range(2)]))
          # btn_dict = {
          #      'a':a,
          #      'b':b
          # }
          # print(btn_dict)
          

          # prize_x = prize[0]
          # prize_y = prize[1]
          
          # print(a[0], b[0], prize_x)
          # print(a[1], b[1], prize_y)
          
          # # print(prize_x)
          # # print(prize_y)

          # print('X possible?')
          # print(is_possible(a[0],b[0],prize_x), '\n')
          # print(prize[0]/gcd(a[0],b[0]))

          # print('Y possible?')
          # print(is_possible(a[1],b[1],prize_y), '\n')
          # print(prize[1]/gcd(a[1],b[1]))

        # winning_combos = []
        # for i in range(1,200):
        #     combinations = list(combinations_with_replacement(['a','b'],r=i))
        #     for c in combinations:
        #         comb_x = [btn_dict[x][0] for x in c]
        #         comb_y = [btn_dict[x][1] for x in c]
        #         # print(sum(comb_x), sum(comb_y), '\n')
        #         if sum(comb_x) == prize_x and sum(comb_y) == prize_y:
        #             winning_combos.append(c)
        
        # if not winning_combos:
        #     continue

        # cheapest = dict(Counter(winning_combos[0]))
        # for i in winning_combos[1:]:
            
        #     j = dict(Counter(i))
        #     if 3*j['a'] + j['b'] < 3*cheapest['a']+cheapest['b']:
        #         cheapest = j

        # total += 3*cheapest['a'] + cheapest['b']
        # print(cheapest)

#     print(total)
        # a is 3 b is 1 
