from re import findall
from pprint import pprint

if __name__ == "__main__":
    with open('14.txt', 'r') as file:
        txt = file.read().splitlines()

    p0s = []
    v0s = []
    for i in txt:
        x = [int(u) for u in findall(r"\-?\d+", i)]
        p0s.append((x[0],x[1]))
        v0s.append((x[2],x[3]))

    w = 101
    h = 103
    tiles = [[0 for i in range(w)] for j in range(h)]

    for glo in range(1001,2001):
        tiles = [[0 for i in range(w)] for j in range(h)]
        for i,j in zip(p0s,v0s):
            x,y = i
            x_,y_ = j
            tiles[y][x] += 1
            for k in range(1,glo):
                tiles[y][x] -= 1

                x = (x + x_) % w
                y = (y + y_) % h

                tiles[y][x] += 1
        
        print('Final state')
        pprint(tiles)

        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j] == 0:
                    tiles[i][j] = '.'


        output_str = "\n".join([str(tile) for tile in tiles])
        with open('output.txt', 'a') as file:
            file.write(f'\n\n After {glo} seconds: \n\n')
            file.write(output_str)



    # mid_w = int(((w - 1) / 2) + 1)
    # mid_h = int(((h - 1) / 2) + 1)

    # top_left = []
    # top_right = []
    # btm_left = []
    # btm_right = []

    # for i in range(mid_h-1):
    #     for j in range(mid_w-1):
    #         top_left.append(tiles[i][j])

    #     for j in range(mid_w,w):
    #         top_right.append(tiles[i][j])

    # for i in range(mid_h, h):
    #     for j in range(mid_w-1):
    #         btm_left.append(tiles[i][j])

    #     for j in range(mid_w,w):
    #         btm_right.append(tiles[i][j])
  

    # safety_factor = sum(top_left) * sum(top_right) * sum(btm_left) * sum(btm_right)

    # print(safety_factor)
    