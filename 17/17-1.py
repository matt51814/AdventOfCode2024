with open('17.txt', 'r') as file:
    txt = file.read().splitlines()

print(txt)

for i in txt:
    if i == '':
        continue
    if 'A' in i:
        A = int(i.split(' ')[-1])
    elif 'B' in i:
        B = int(i.split(' ')[-1])
    elif 'C' in i:
        C = int(i.split(' ')[-1])
    else:
        prog = [int(x) for x in i.split(' ')[-1].split(',')]

jumped = False
pointer = 0
result = []
print(A,B,C,prog)
while pointer < len(prog):
    combo = {
        0:0,
        1:1,
        2:2,
        3:3,
        4:A,
        5:B,
        6:C,
        7:None
    }

    
    try:
        opcode = prog[pointer]
    except IndexError:
        break
    operand = prog[pointer+1]

    match opcode:
        case 0:
            num = A
            denom = 2 ** combo[operand]
            A = int(num/denom)
        case 1:
            B = B ^ operand
        case 2:
            B = combo[operand] % 8
        case 3:
            if A == 0:
                pass
            else:
                pointer = operand
                continue
        case 4:
            B = B^C
        case 5:
            tmp = str(combo[operand] % 8)
            if len(tmp) > 1:
                for i in tmp:
                    result.append(int(i))
            else:
                result.append(int(tmp))
        case 6:
            num = A
            denom = 2 ** combo[operand]
            B = int(num/denom)
        case 7:
            num = A
            denom = 2 ** combo[operand]
            C = int(num/denom)
        case _:
            pass
    

    
    pointer += 2
    
print(result)
