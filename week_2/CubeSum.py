n = int(input())

if n <= 1:
    print(0)

j = int(n**(1/3)) + 1
i = 1

pair_count = 0

while i <= j:
    if i**3 + j**3 == n:
        pair_count += 1
        i += 1
        j -= 1
    elif i**3 + j**3 < n:
        i += 1
    else:
        j -= 1

print(pair_count)