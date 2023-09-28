met_max = False
met_second_max = False

cur_el = int(input())


while cur_el:
    if not met_max:
        max_ = cur_el
        met_max = True
    elif (not met_second_max) and cur_el != max_:
        max_, second_max = max(max_, cur_el), min(max_, cur_el)
        met_second_max = True
    elif cur_el > max_:
        max_, second_max = cur_el, max_
    elif cur_el < max_ and cur_el > second_max:
        second_max = cur_el
    
    cur_el = int(input())


if not met_second_max:
    print("NO")
else:
    print(second_max)