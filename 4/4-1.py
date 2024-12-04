def create_directional_dict(row,col, wordsearch):
    graph = {}
    start = wordsearch[row][col]
    if col >= 3:
        graph['left'] = start + wordsearch[row][col-1] + wordsearch[row][col-2] + wordsearch[row][col-3]

        if row >= 3:
            graph['up-left'] = start + wordsearch[row-1][col-1] + wordsearch[row-2][col-2] + wordsearch[row-3][col-3]

        if row <= len(wordsearch) - 4:
            graph['bottom-left'] = start + wordsearch[row+1][col-1] + wordsearch[row+2][col-2] + wordsearch[row+3][col-3]

    if col <= len(wordsearch[row]) - 4:
        graph['right'] = start + wordsearch[row][col+1] + wordsearch[row][col+2] + wordsearch[row][col+3]

        if row >= 3:
            graph['up-right'] = start + wordsearch[row-1][col+1] + wordsearch[row-2][col+2] + wordsearch[row-3][col+3]

        if row <= len(wordsearch) - 4:
            graph['bottom-right'] = start + wordsearch[row+1][col+1] + wordsearch[row+2][col+2] + wordsearch[row+3][col+3]

    if row >= 3:
        graph['up'] = start + wordsearch[row-1][col] + wordsearch[row-2][col] + wordsearch[row-3][col]

    if row <= len(wordsearch) - 4:
        graph['down'] = start + wordsearch[row+1][col] + wordsearch[row+2][col] + wordsearch[row+3][col]

    return graph

    


if __name__ == '__main__':
    with open('4.txt', 'r') as file:
        txt = file.read().splitlines()

    xmas_count = 0
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            dir_dict = create_directional_dict(i,j,txt)
            for vals in dir_dict.values():
                if vals == 'XMAS':
                    xmas_count += 1

		
  
    print(xmas_count)
