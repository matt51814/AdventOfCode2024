class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


dir_dict = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}
check_next = {
    'right': (0, 1),
    'left': (0, -1),
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

def detect_loop(head):

    # Fast and slow pointers initially points to the head
    slow = head
    fast = head

    # Loop that runs while fast and slow pointer are not
    # None and not equal
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow == fast:
            return True
    return False




    # # Loop that runs while fast and slow pointer are not
    # # None and not equal
    # while slow.next:
    #     while fast.next:
    #         fast = fast.next
    #         if slow.data == fast.data:
    #             return True
    #     slow = slow.next

    # return False


if __name__ == '__main__':
    with open('6-ex.txt', 'r') as file:
        txt = file.read().splitlines()
    
    x, y = find_start_position(txt)

    dir = 'up'
    
    def _change_pos(x,y):
        x_, y_ = dir_dict[dir]
        return x+x_, y+y_

    def _check_next(x,y):
        x_, y_ = check_next[dir]
        return x+x_, y+y_


    visited = [[x,y]]
    while 0 <= x <= len(txt)-1 and 0 <= y <= len(txt[0])-1:
        x_, y_ = _check_next(x,y)
        try:
            if txt[x_][y_] == "#":
                dir = change_dir[dir]
        except IndexError:
            break
        x, y = _change_pos(x,y)
        visited.append([x,y])
    
    distinct = []
    for v in visited:
        if v not in distinct and v != list(find_start_position(txt)):
            distinct.append(v)

    print(distinct)
    print(len(distinct))

    obstructions = []
    
    for i in distinct:
        
        print(i)

        x, y = find_start_position(txt)
        dir = 'up'
        tmp_txt = txt.copy()
        xp, yp = i
        new_string = ""
        for idx, val in enumerate(tmp_txt[xp]):
            if idx == yp:
                new_string += 'O'
            else:
                new_string += val
        tmp_txt[xp] = new_string

        # visited = 0
        cycle_list = []
        cycle_set = set()
        visited = 0
        llist = LinkedList()
        while 0 <= x <= len(txt)-1 and 0 <= y <= len(txt[0])-1:
            llist.append((x,y))
            if detect_loop(llist.head):
                obstructions.append(i)
                break
            x_, y_ = _check_next(x,y)

            try:
                if tmp_txt[x_][y_] == "#":
                    dir = change_dir[dir]
            except IndexError:
                break

            if tmp_txt[x_][y_] == 'O':
                dir = change_dir[dir]

                
            x, y = _change_pos(x,y)



            # if visited >= 1:
            #     cycle_list.append((x,y))
            #     cycle_set.add((x,y))
            #     if len(cycle_list) > len(cycle_set) and \
            #         len((set(cycle_list))) == len(cycle_set) and \
            #             cycle_list[0] == cycle_list[-1]:
            #         obstructions.append(i)

            #         break


            # if visited > 1:
            #     obstructions.append(i)
            #     break
    
    print(len(obstructions))
