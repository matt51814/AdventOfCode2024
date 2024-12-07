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


if __name__ == '__main__':
    with open('6.txt', 'r') as file:
        txt = file.read().splitlines()
    
    x, y = find_start_position(txt)

    dir = 'up'
    
    def _change_pos(x,y):
        x_, y_ = dir_dict[dir]
        return x+x_, y+y_

    for i in range(len(txt)):
        for j in range(len(txt[0])):
            txt[i][j] = '#'
            visited = [[x,y]]
            while 0 <= x <= len(txt)-1 and 0 <= y <= len(txt[0])-1:
                print(x,y)
                x_, y_ = _change_pos(x,y)
                try:
                    if txt[x_][y_] == "#":
                        dir = change_dir[dir]
                except IndexError:
                    break
                x, y = _change_pos(x,y)
                visited.append([x,y])
            txt[i][j] = '.'

                
    distinct = []
    for v in visited:
        if v not in distinct:
            distinct.append(v)

    print(len(distinct))