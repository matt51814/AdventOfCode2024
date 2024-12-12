
def is_neighbour(x1, y1, x2, y2):
    return (x1 in (x2-1, x2+1) and y1 == y2) or \
           (x1 == x2 and y1 in (y2+1, y2-1))

def is_value_touching_group(val, groups, x, y):
    for d in groups:
        if d['color'] == val and any(is_neighbour(x, y, *cell) for cell in d['cells']):
            return d

def check(m, w, h):
    groups = []

    for i in range(h):
        for j in range(w):
            val = m[i*w + j]
            touching_group = is_value_touching_group(val, groups, i, j)
            if touching_group:
                touching_group['cells'].append( (i, j) )
            else:
                groups.append({'color':val, 'cells':[(i, j)]})

    final_groups = []
    while groups:
        current_group = groups.pop()
        for c in current_group['cells']:
            touching_group = is_value_touching_group(current_group['color'], groups, *c)
            if touching_group:
                touching_group['cells'].extend(current_group['cells'])
                break
        else:
            final_groups.append(current_group['cells'])

    return final_groups

def get_areas(li: list[list]):
    areas = []
    for i in li:
        areas.append(len(i))
    return areas


def get_perimeters(li: list[list]):
    result = []
    for ex in li:
        total_boxes = 4 * len(ex)
        connecting = 0
        for i in ex:
            x,y = i
            for j in ex:
                if i == j:
                    continue
                x_, y_ = j
                if (x_-x)**2 + (y_-y)**2 < 2:
                    connecting += 1
        result.append(total_boxes - connecting)

    return result

if __name__ == "__main__":
    with open('12.txt', 'r') as file:
        txt = file.read().splitlines()

    h = len(txt)
    w = len(txt[0])

    unique_terms = set()
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            unique_terms.add(txt[i][j])


    rename_dict = {val:idx for idx, val in enumerate(unique_terms)}

    new_txt = []
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            new_txt.append(rename_dict[txt[i][j]])


    segmented = check(new_txt, w, h)

    total = 0
    for i,j in zip(get_areas(segmented), get_perimeters(segmented)):
        total += i * j
    
    print(total)