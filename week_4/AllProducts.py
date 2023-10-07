def factorizations(n, prev_min = 2, prev_vals = []):
    if n == 1:
        print('*'.join(prev_vals))
        return
    for i in range(prev_min, n + 1):
        if not(n % i) and (n // i >= max(prev_min, i)):
            prev_vals.append(str(i))
            factorizations(n // i, i, prev_vals)
            prev_vals.pop(-1)   
    
    i = n
    prev_vals.append(str(i))
    factorizations(n // i, i, prev_vals)
    prev_vals.pop(-1)
    


n = int(input())
if n == 1:
    print(1)
else:
    factorizations(n)