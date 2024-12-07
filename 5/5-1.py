
if __name__ == '__main__':
    with open('5.txt', 'r') as file:
        txt = file.read().splitlines()

    ord_rules = [x for x in txt if '|' in x]
    updates = [x for x in txt if '|' not in x and x!='']

    after_graph = {}
    for x in ord_rules:
        _x = x.split('|')
        if _x[0] not in after_graph.keys():
            after_graph[_x[0]] = [_x[1]]
        else:
            after_graph[_x[0]].append(_x[1])



    before_graph = {}
    for x in ord_rules:
        _x = x.split('|')
        if _x[1] not in before_graph.keys():
            before_graph[_x[1]] = [_x[0]]
        else:
            before_graph[_x[1]].append(_x[0])


    # def bfs(graph, node): #function for BFS
    #     visited = [node] # List for visited nodes.
    #     queue = [node]     #Initialize a queue
    #     result = []
    #     while queue:          # Creating loop to visit each node
    #         m = queue.pop(0) 
    #         result.append(m)
    #         if m in graph.keys():

    #             # for neighbour in graph[m]:
    #             #     if neighbour not in visited:
    #             #         visited.append(neighbour)
    #             #         queue.append(neighbour)

    #     return result



    def _check_valid_after(idx, val, li) -> bool:
        after_list = []
        if val not in after_graph.keys():
            return True
        for i in after_graph[val]:
            if i in li:
                after_list.append(i)
        for i in li[idx+1:]:
            if i not in after_list:
                return False
        return True
    
    def _check_valid_before(idx, val, li) -> bool:
        before_list = []
        if val not in before_graph.keys():
            return True
        for i in before_graph[val]:
            if i in li:
                before_list.append(i)
        print(before_list)
        for i in li[:idx]:
            if i not in before_list:
                return False
        return True

    
    # def _check_valid_after(idx, val, li) -> bool:
    #     after_list = bfs(after_graph, val, li)
    #     if not after_list:
    #         return True
    #     for i in li[idx:]:
    #         if i not in after_list:
    #             print(i)
    #             return False
    #     return True
    
    # def _check_valid_before(idx, val, li) -> bool:
    #     before_list = bfs(before_graph, val, li)
    #     if not before_list:
    #         return True
    #     for i in li[:idx]:
    #         if i not in before_list:
    #             print(i)
    #             return False
    #     return True


    def check_valid(idx: int, val: int, li: list) -> bool:
        if idx == 0:
            valid = _check_valid_after(idx, val, li)
        elif idx == len(li)-1:
            valid = _check_valid_before(idx, val, li)
        else:
            valid = _check_valid_after(idx, val, li) and _check_valid_before(idx, val, li)
        return valid
    
    def find_middle(input_list):
        middle = float(len(input_list))/2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return (input_list[int(middle)], input_list[int(middle-1)])
        
    total = 0
    # print(check_valid(1, '47',updates[0].split(',')))
    
    
    for update in updates:
        _update = update.split(',')
        print(_update)
        update_bools = []
        for idx, val in enumerate(_update):
            update_bools.append(check_valid(idx,val,_update))
        print(all(update_bools))
        if all(update_bools):
            total += int(find_middle(_update))

    print(total)


