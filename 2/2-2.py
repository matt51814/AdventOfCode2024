f = open("2.txt", "r")

list_of_lists = []
for i in f.readlines():
    tmp = []
    for j in i.strip().split(' '):
        tmp.append(int(j))
    list_of_lists.append(tmp)

def check_ascending(li) -> bool:
    for i in range(len(li)-1):
        if li[i+1] <= li[i]:
            return False
    return True

def check_descending(li) -> bool:
    for i in range(len(li)-1):
        if li[i+1] >= li[i]:
            return False
    return True

def check_adj(li) -> bool:
    for i in range(len(li)-1):
        if abs(li[i+1]-li[i]) == 0:
            return False
        elif abs(li[i+1]-li[i]) > 3:
            return False
    return True



if __name__ == "__main__":
    safe = []
    for li in list_of_lists:
        # if either increasing or decreasing
        if any(
            (check_descending(li), check_ascending(li))
        ):
            if check_adj(li):
                safe.append(li)
                continue
    
        diff_list = []
        for i in range(len(li)-1):
            diff_list.append(li[i+1] - li[i])
        
        diff_diff_list = []
        for i in range(len(diff_list)-1):
            diff_diff_list.append(diff_list[i+1] - diff_list[i])


        print(li)
        print(diff_list)

        in_range = len(list(filter(lambda x: 0 < x <= 3, [abs(x) for x in diff_list])))

        num_pos = len(list(filter(lambda x: x > 0, diff_list)))
        num_neg = len(list(filter(lambda x: x < 0, diff_list)))
        



        errors = len(diff_list) - in_range
        print(errors)
        if errors == 1:
            safe.append(li)

    print(len(safe))

        