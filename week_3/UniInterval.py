intervals = list(eval(input()))
intervals.sort(key = lambda x: x[0])


l = 0
if len(intervals):
    cur_min = intervals[0][0]
    cur_max = intervals[0][1]
for interval in intervals:
    a, b = interval
    if a >= cur_max:
        l += (cur_max - cur_min)
        cur_min, cur_max = a, b
    else:
        cur_max = max(cur_max, b)
    

l += (cur_max - cur_min)
print(l)