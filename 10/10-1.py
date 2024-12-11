def find_zeros(txt):
    zeros = []
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] == '0':
                zeros.append((i,j))
    return zeros

def check_adjacent(txt, pos):
    """
    Return the adjacent posititons given a reference position
    """    
    return_positions = []
    x,y = pos
    val = int(txt[x][y])
    if 0 <= x-1:
        if int(txt[x-1][y]) - 1 == val:
            # check above
            return_positions.append((x-1,y))
    if x+1 < len(txt):
        if int(txt[x+1][y]) - 1 == val:
            # check below
            return_positions.append((x+1,y))
    if 0 <= y-1:
        if int(txt[x][y-1]) - 1 == val:
            # check left
            return_positions.append((x,y-1))
    if y+1 < len(txt[x]):
        if int(txt[x][y+1]) - 1 == val:
            # check right
            return_positions.append((x,y+1))
    
    return return_positions

def make_adjacency_matrix(txt):
    graph = {}
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            graph[(i,j)] = check_adjacent(txt, (i,j))
    return graph


def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (txt[m[0]][m[1]], end = " ") 
    print (len(check_adjacent(txt,m))==1)
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

if __name__ == "__main__":
    with open('10.txt', 'r') as file:
        txt = file.read().splitlines()

    graph = make_adjacency_matrix(txt)
    visited = [] # List for visited nodes.
    queue = [] #Initialize a queue

    total = 0
    for zero in find_zeros(txt):
        visited = []
        queue = []
        bfs(visited,graph,zero)
        value_list = [txt[i[0]][i[1]] for i in visited]
        nine_list = list(filter(lambda x: x == '9', value_list))
        total += len(nine_list)

    print(total)
