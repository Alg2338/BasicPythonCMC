res = 0

prev = input()
s = prev
n = len(prev)

while s and s != '':
    i = 0
    while i < n:
        if (s[i] == '.') and (prev[i] == '#'):
            res += 1
            while (i < n) and (s[i] != prev[i]):
                i += 1
            
            

        i += 1
    prev = s
    try:
        s = input()
    except:
        break
    
        
res += len(list(filter(None, prev.split('.'))))
print(res)