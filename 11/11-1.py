

def stone_rules(num):
    if int(num) == 0:
        return [1]
    if len(num) % 2 == 0:
        return [int(num[:int(len(num)/2)]), int(num[int(len(num)/2):])]
    return [int(num) * 2024]
# If the stone is engraved with the number 0, 
# it is replaced by a stone engraved with the number 1.

# If the stone is engraved with a number that has an even number of digits, 
# it is replaced by two stones. 
# The left half of the digits are engraved on the new left stone, 
# and the right half of the digits are engraved on the new right stone. 
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
 
# If none of the other rules apply, 
# the stone is replaced by a new stone; 
# the old stone's number multiplied by 2024 is engraved on the new stone.





if __name__ == "__main__":
    with open('11.txt', 'r') as file:
        txt = file.read()
    first_list = txt.split(' ')
    tmp_list = first_list.copy()
    blink = 0
    print('Initial blink')
    print(first_list)
    for i in range(1,26):
        blink += 1
        skip_idx = -1
        new_list = tmp_list.copy()
        for idx, val in enumerate(new_list):
            if idx == skip_idx:
                continue
            x = stone_rules(val)
            if len(x) == 1:
                # update value at index
                new_list[idx] = str(x[0])
            else:
                # split value in half
                new_list.pop(idx)
                new_list.insert(idx, str(x[0]))
                new_list.insert(idx+1, str(x[1]))
                skip_idx = idx+1

        print(f"After {blink} blink")
        print(new_list)
        tmp_list = new_list.copy()
    print(len(new_list))