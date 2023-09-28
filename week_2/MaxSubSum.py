cur_el = int(input())
res = cur_el
cur_sum = cur_el


while cur_el:
    if cur_sum > res:
        res = cur_sum
    
    cur_sum = max(cur_sum, 0)

    cur_el = int(input())
    cur_sum += cur_el

print(res)

