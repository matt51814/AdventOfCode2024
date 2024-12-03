f = open("2.txt", "r")

list_of_lists = []
for i in f.readlines():
    tmp = []
    for j in i.strip().split(' '):
        tmp.append(int(j))
    list_of_lists.append(tmp)

f.close()

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


def is_valid(li: list) -> bool:
    if any(
        (check_descending(li), check_ascending(li))
    ):
        if check_adj(li):
            return True
    return False

if __name__ == "__main__":
    safe = 0
    for li in list_of_lists:
        if is_valid(li):
            safe += 1
            continue
    
        # on remaining lists we just pop one element and check if its alright
        for i in range(len(li)):
            tmpli = li.copy()
            tmpli.pop(i)
            if is_valid(tmpli):
                safe += 1
                break

    
    print(safe)

        