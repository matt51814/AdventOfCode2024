
def get_freq_locs(txt):
    freq_locs = []
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j].isalnum():
                freq_locs.append((i,j))
    return freq_locs

def get_line(freq1, freq2):
    x1, y1 = freq1
    x2, y2 = freq2

    x_ = x2 - x1
    y_ = y2 - y1

    return [(x1 - x_, y1 - y_), (x2 + x_, y2 + y_)]

def valid_point(freq, txt):
    x, y = freq
    print(x,y)
    if 0 <= x < len(txt) and 0 <= y < len(txt[0]):
        return True
    return False

if __name__ == "__main__":


    with open('8.txt', 'r') as file:
        txt = file.read().splitlines()

    antinodes = []
    freq_locs = get_freq_locs(txt)
    for idx, val in enumerate(freq_locs):
        for i,j in enumerate(freq_locs):
            if idx == i:
                continue
            if txt[val[0]][val[1]] != txt[j[0]][j[1]]:
                continue
            for k in get_line(val, j):
                if valid_point(k, txt):
                    antinodes.append(k)
    
    print(antinodes)
    print(len(antinodes))

    unique_antinodes  = []
    for node in antinodes:
        if node not in unique_antinodes:
            unique_antinodes.append(node)

    print(unique_antinodes)
    print(len(unique_antinodes))