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
    with open('15-ex.txt', 'r') as file:
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

    pprint(map)
    print(moves)

    print(len(map[0]))

    # If the tile is #, the new map contains ## instead.
    # If the tile is O, the new map contains [] instead.
    # If the tile is ., the new map contains .. instead.
    # If the tile is @, the new map contains @. instead.

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                map[i][j] = '##'
            elif map[i][j] == 'O':
                map[i][j] = '[]'
            elif map[i][j] == '.':
                map[i][j] = '..'
            elif map[i][j] == '@':
                map[i][j] = '@.'

    new_map = []
    for i in map:
        new_map.append(list("".join(i)))

    map = new_map.copy()
      
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '@':
                start_pos = (i,j)

    print(start_pos)
    # with open('output.txt','w') as file:
    #     print(map,file=file)
    


    x,y = start_pos
    print(f'\n\n Initial \n')
    for i in moves[:7]:
        
        pprint(map)
        print(f'\n\n Direction: {i} \n')
        
        x_, y_ = move((x,y), i)
        if map[x_][y_] == '#':
            continue

        if i in ['<','>']:
            if map[x_][y_] in ['[',']']:
                a, b = x_, y_
                mv = 0
                hit = [(a,b)]
                while True:
                    mv += 1
                    a, b = move((a,b),i)
                    hit.append((a,b))
                    if map[a][b] in ['.','#']:
                        break
            
                hit_vals = [map[x][y] for x,y in hit]
                if hit_vals[-1] == '#':
                    continue
                if hit_vals[-1] == '.':
                    for idx, val in enumerate(hit):
                        x0, y0 = val
                        if idx == 0:
                            map[x0][y0] = '.'
                        else:
                            v = hit_vals.pop(0)
                            map[x0][y0] = v
        
        
        
        if i in ['v', '^']:
            if map[x_][y_] in ['[',']']:
                a, b = x_, y_
                height = 0
                layers = []
                while True:
                    if map[a][b] == '.':
                        hit = '.'
                        break
                    if map[a][b] == '#':
                        hit = '#'
                        break
                    height += 1
                    # check width right
                    width_r = 0
                    b_ = b
                    while True:
                        b_ += 1
                        if map[a][b_] in ['[', ']']:
                            width_r += 1
                        else:
                            break

                    # check width left
                    width_l = 0
                    b_ = b
                    while True:
                        b_ -= 1
                        if map[a][b_] in ['[', ']']:
                            width_l += 1
                        else:
                            break
                    layers.append((height,width_r,width_l))


                    a, b = move((a,b), i)
                
                if hit == '#':
                    continue
                
                # starting with top layer
                for l in layers[::-1]:
                    h,wr,wl = l
                    a, b = x, y
                    
                    # replace immediately above pos
                    map[a-h-1][b] = map[a-h][b]
                    map[a-h][b] = '.' 

                    # replace left
                    for i in range(wl+1):
                        map[a-h-1][b-(i+1)] = map[a-h][b-(i+1)]
                        map[a-h][b-(i+1)] = '.' 
                    
                    # replace right
                    for i in range(wr+1):
                        map[a-h-1][b+i+1] = map[a-h][b+i+1]
                        map[a-h][b+i+1] = '.' 

                print(height)
                print(layers)


        
        map[x][y] = '.'
        x, y = x_, y_
        map[x][y] = '@'


    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                total += 100*i + j
    print(total)