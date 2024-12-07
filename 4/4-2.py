def create_directional_dict(row,col, wordsearch):
    graph = {}
    start = wordsearch[row][col]
    if col >= 1 and row >= 1 and col <= len(wordsearch[row]) - 2 and row <= len(wordsearch) - 2:
        graph['up-left'] = wordsearch[row-1][col-1] + start + wordsearch[row+1][col+1] 
        graph['bottom-left'] = wordsearch[row+1][col-1] + start + wordsearch[row-1][col+1] 
        graph['bottom-right'] = graph['up-left'][::-1]
        graph['top-right'] = graph['bottom-left'][::-1]

    return graph

if __name__ == '__main__':
    with open('4.txt', 'r') as file:
        txt = file.read().splitlines()

    xmas_count = 0
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            dir_dict = create_directional_dict(i,j,txt)
            mas_count = 0
            for val in dir_dict.values():
                if val == 'MAS':
                    mas_count += 1
            if mas_count == 2:
                xmas_count +=1

    print(xmas_count)
