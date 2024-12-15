from pprint import pprint

move_dict = {
    '^': (-1,0),
    'v': (1,0),
    '<': (0,-1),
    '>': (0,1)
}

def move(p0,dir):
    x0, y0 = p0
    x_, y_ = move_dict[dir]
    return (x0 + x_, y0 + y_)

if __name__ == "__main__":
    with open('15.txt', 'r') as file:
        txt = file.read().splitlines()

    print(txt)

    map = []
    moves = ""
    swap = False
    for i in txt:
        if i == '':
            swap = True 
            continue
        if swap:
            moves += i
        else:
            map.append(list(i))

    print(map)
    print(moves)

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '@':
                start_pos = (i,j)

    print(start_pos)
    pprint(map)
    x,y = start_pos
    for i in moves:
        print(i)
        x_, y_ = move((x,y), i)
        if map[x_][y_] == '#':
            continue
        if map[x_][y_] == 'O':
            
            a, b = x_, y_
            mv = 0
            hit = ''
            while True:
                mv += 1
                a, b = move((a,b),i)
                if map[a][b] == '.':
                    hit = '.'
                    break
                if map[a][b] == '#':
                    hit = '#'
                    break

            print(mv)
            print(hit)
            if hit == '.':
                map[x_][y_] = '.'
                a,b = x_,y_
                for j in range(mv):
                    a,b = move((a,b),i)
                    map[a][b] = 'O'
            elif hit == '#':
                continue
                    

        map[x][y] = '.'
        x, y = x_, y_
        map[x][y] = '@'
        print(x,y)
        pprint(map)

    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                total += 100*i + j
    print(total)
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########