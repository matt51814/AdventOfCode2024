from itertools import repeat

if __name__ == "__main__":
    with open('9.txt', 'r') as file:
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
            for u, v in enumerate(result[:idx:-1]):
                if v != '.':
                    result[idx] = result[-(u+1)]
                    result[-(u+1)] = '.'
                    break

    print(result)

    total = 0
    for i,j in zip(range(len(result)), result):
        if j == '.':
            break
        total += i*j 

    print(total)