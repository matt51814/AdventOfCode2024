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
        
        while not check_all_valid(array):
            gap = 1
            # FORWARD PASS ->
            # Loop from the second element of the array until
            # the last element
            for i in range(gap, len(array)):
                # This is the element we want to position in its
                # correct place
                key_item = array[i]

                # Initialize the variable that will be used to
                # find the correct position of the element referenced
                # by `key_item`
                j = i - gap
                # Run through the list of items (the left
                # portion of the array) and find the correct position
                # of the element referenced by `key_item`. Do this only
                # if `key_item` is smaller than its adjacent values.
                # while j >= 0 and array[j] > key_item:
                while j >= 0 and not check_valid(j, array[j], array):
                    # Shift the value one position to the left
                    # and reposition j to point to the next element
                    # (from right to left)
                    array[j + gap] = array[j]
                    j -= 1

                # When you finish shifting the elements, you can position
                # `key_item` in its correct location
                array[j + gap] = key_item

            # BACKWARD PASS <-
            # Loop from the second element of the array until
            # the last element
            for i in range(0, len(array))[::-1]:
                # This is the element we want to position in its
                # correct place
                key_item = array[i]

                # Initialize the variable that will be used to
                # find the correct position of the element referenced
                # by `key_item`
                j = i + gap

                # Run through the list of items (the left
                # portion of the array) and find the correct position
                # of the element referenced by `key_item`. Do this only
                # if `key_item` is smaller than its adjacent values.
                # while j >= 0 and array[j] > key_item:
                while j <= len(array)-1 and not check_valid(j, array[j], array):
                    # Shift the value one position to the left
                    # and reposition j to point to the next element
                    # (from right to left)
                    array[j - gap] = array[j]
                    j += 1

                # When you finish shifting the elements, you can position
                # `key_item` in its correct location
                array[j - gap] = key_item
            print(array)
            time.sleep(2)

        return array


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


