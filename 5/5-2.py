import time
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
        for i in li[:idx]:
            if i not in before_list:
                return False
        return True


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
    

    def sort(li) -> list:
        for idx, val in li:
            if check_valid(idx, val, li):
                continue


    def check_all_valid(li):
        bool_list = []
        for idx, val in enumerate(li):
            bool_list.append(check_valid(idx, val, li))
        return all(bool_list)

    def sort(array):
        numbers_to_add = array.copy()
        sorted = []
        tmp_list = []

        # while we still have numbers to add
        while numbers_to_add:
            # loop through the numbers remaining to add
            for i in numbers_to_add:
                # at each position in the current result list
                for j in range(len(tmp_list)+1):
                    tmp_list = sorted.copy()
                    tmp_list.insert(j,i)
                    if check_all_valid(tmp_list):
                        numbers_to_add.remove(i)
                        sorted = tmp_list.copy()
                        break
        
        return sorted


    incorrect = []
    for update in updates:
        _update = update.split(',')
        update_bools = []
        for idx, val in enumerate(_update):
            update_bools.append(check_valid(idx,val,_update))
        if not all(update_bools):
            incorrect.append(_update)


    total = 0

    for inc in incorrect:            
        print(inc)
        sorted = sort(inc)
        print(sorted)
        total += int(find_middle(sorted))

    print(total)


