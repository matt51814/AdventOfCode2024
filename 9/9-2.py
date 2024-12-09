from itertools import repeat

def find_gap(idx, result, term):
    gap = 0   
    for i in result[idx:]:
        if i == term:
            gap += 1
        else:
            break
    return gap

if __name__ == "__main__":
    with open('9-ex.txt', 'r') as file:
        txt = file.read()
    print(txt)


    # txt = '12345'

    id = 0
    result = []
    for i in range(len(txt)):
        if i % 2 == 0:
            result.extend(list(repeat(id,int(txt[i]))))
            id += 1
        else:
            result.extend(list(repeat('.',int(txt[i]))))
        
    
    print(result)

    for idx, val in enumerate(result):
        if val == '.':


            dot_gap = find_gap(idx, result, '.')
            tmp = 0
            for u, v in enumerate(result[:idx:-1]):
                if u < tmp:
                    continue

                if v != '.':

                    gap = find_gap(u, result[:idx:-1], v)

                    if gap <= dot_gap:
                        
                        for j in range(gap):

                            result[idx+j] = result[-(u+1+j)]
                            result[-(u+1+j)] = '.'
                        dot_gap = dot_gap - gap
                        tmp = u + dot_gap
                        
                        

    print(result)

    total = 0
    for i,j in zip(range(len(result)), result):
        if j == '.':
            break
        total += i*j 

    print(total)