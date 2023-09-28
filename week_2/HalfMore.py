cur_el = input()
res = cur_el
c = 1
while cur_el and cur_el != '':
    cur_el = input()
    if cur_el == res:
        c += 1
    else:
        c -= 1
    
    if c < 0:
        res = cur_el
        c = 1
    
print(eval(res))