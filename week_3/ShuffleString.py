b = input()
a = input()
# print(a, b, sep = '   P   ')

if len(a) != len(b):
    print("No")
else:
    found_n = False
    for n in range(1, len(b) + 1):

        shuffled_b = ''
        for k in range(n):
            shuffled_b += b[k::n]
        
        # print(n, a, shuffled_b, sep = ' ll ')

        if shuffled_b == a:
            print(n)
            found_n = True
            break
    
    if not found_n:
        print("No")