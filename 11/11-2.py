def stone_rules(num):
    if int(num) == 0:
        return [1]
    if len(num) % 2 == 0:
        z = int(len(num)/2)
        return [int(num[:z]), int(num[z:])]
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


def my_generator(li):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < len(li):

        # produce the current value of the counter
        yield value, li[value]

        # increment the counter
        value += 1


if __name__ == "__main__":
    with open('11.txt', 'r') as file:
        txt = file.read()
    first_list = txt.split(' ')
    new_list = first_list.copy()
    blink = 0
    print('Initial blink')
    print(first_list)
    y = 1
    while y < 76:
        blink += 1
        skip_idx = -1
        # new_list = tmp_list.copy()
        for i,v in my_generator(new_list):
        #for idx, val in enumerate(new_list):
            if i == skip_idx:
                continue
            x = stone_rules(v)
            if len(x) == 1:
                # update value at index
                new_list[i] = str(x[0])
            else:
                # split value in half
                new_list[i] = str(x[0])
                new_list.insert(i+1, str(x[1]))
                skip_idx = i+1

        print(f"After {blink} blink")
        print(new_list)
        # tmp_list = new_list.copy()
        y += 1
    print(len(new_list))