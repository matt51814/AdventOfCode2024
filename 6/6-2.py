import time 

dir_dict = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}
change_dir = {
    'up': 'right',
    'left': 'up',
    'down': 'left',
    'right': 'down'
}

# if there's something directly to the right of the direction then turn
# left 90 degrees


def find_exit_position(map: list[list[str]]):
    # check top
    for i in range(len(map[0])):
        if map[0][i] == 'X' and map[1][i] == 'X':
            return 0, i, 'up'
    # check right
    for i in range(len(map)):
        if map[i][-2] == 'X' and map[i][-1] == 'X':
            return i, len(map)-1, 'right'
    # check bottom
    for i in range(len(map[0])):
        if map[len(map)-2][i] == 'X' and map[len(map)-1][i] == 'X':
            return len(map)-1, i, 'down'
    # check left
    for i in range(len(map)):
        if map[i][0] == 'X' and map[i][1] == 'X':
            return i, 0, 'left'


def find_start_position(txt):
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] == '^':
                return (i,j)

def has_cycle(li):
    if list(set(li)) == li:
        return False
    # need to determine if we have a cycle
    for i in range(len(li)):
        if len(set(li[i:])) == len(li[i:]) / 2:
            return True
    return False

def in_bounds(x,y,map):
    if 0 <= x <= len(map)-1 and 0 <= y <= len(map[0])-1:
        return True
    return False


def _change_pos(x,y):
    x_, y_ = dir_dict[dir]
    return x+x_, y+y_





if __name__ == '__main__':
    with open('6.txt', 'r') as file:
        txt = file.read().splitlines()
    
    x_s, y_s = find_start_position(txt)

    txt = [list(x) for x in txt]
    obstructions = 0
    pos = 1
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            print("Position: ", pos, i, j)
            if txt[i][j] == '#':
                continue
            txt[i][j] = '#'
            dir = 'up'   
            x, y = x_s, y_s

            visited = []
            while in_bounds(x,y,txt):
                print(x,y)
                visited.append((x,y))
                x_, y_ = _change_pos(x,y)
                if in_bounds(x_,y_,txt): 
                    if txt[x_][y_] == "#":
                        dir = change_dir[dir]
                x, y = _change_pos(x,y)

                if has_cycle(visited):
                    print("OBSTRUCTION FOUND")
                    obstructions += 1
                    break
            
            txt[i][j] = '.'
            pos += 1

    print(obstructions)      
            # distinct = []
            # for v in visited:
            #     if v not in distinct:
            #         distinct.append(v)

            # print(len(distinct))


    # txt = [list(x) for x in txt]
    # # print(txt)
    # obstructions = 0
    # # for i in range(len(txt)):
    # #     for j in range(len(txt[0])):
    #         x, y = x_s, y_s
    #         dir = 'up'
    #         # print(f'# location: ({i},{j})')
    #         txt[i][j] = '#'
    #         visited = [(x,y)]
    #         while 0 <= x <= len(txt)-1 and 0 <= y <= len(txt[0])-1:
    #             # print(visited[-1])
    #             iter_count = 1
    #             x_, y_ = _change_pos(x,y)
    #             try:
    #                 if txt[x_][y_] == "#":
    #                     dir = change_dir[dir]
    #             except IndexError:
    #                 break
    #             x, y = _change_pos(x,y)
    #             visited.append((x,y))
    #             if has_cycle(visited):
    #                 obstructions += 1
    #                 break
    #         txt[i][j] = '.'

