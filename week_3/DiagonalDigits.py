n, m = map(int, input().split(','))


if (n > 0) and (m > 0):
    res = []
    for i in range(m):
        res.append([0] * n)

    i, j = 0, 0 
    i_delta = 1
    j_delta = 0
    val = 0
    while (i < m - 1) or (j < n - 1):
        # change_direction = False
        # print("i = {}, j = {}, val = {}".format(i, j, val))
        # print("i_delta = {}, j_delta = {}".format(i_delta, j_delta))

        res[i][j] = val 
        val = (val + 1) % 10

        new_i = i + i_delta
        if new_i >= 0 and new_i < m:
            i = new_i
        
        new_j = j + j_delta
        if new_j >= 0 and new_j < n:
            j = new_j

        match i_delta, j_delta:
            case 1, 0:
                # handle V
                if n == 1:
                    i_delta, j_delta = 1, 0
                elif j == n - 1:
                    i_delta, j_delta = 1, -1
                else:
                    i_delta, j_delta = -1, 1
                # print('1')
            case 0, 1:
                # handle ->
                if m == 1:
                    i_delta, j_delta = 0, 1
                elif i == m - 1:
                    i_delta, j_delta = -1, 1
                else:
                    i_delta, j_delta = 1, -1
                # print('2')
            case 1, -1:
                # 
                if i == m - 1:
                    i_delta, j_delta = 0, 1
                elif j == 0:
                    i_delta, j_delta = 1, 0
                # print('3')
            case -1, 1:
                if j == n - 1:
                    i_delta, j_delta = 1, 0
                elif i == 0:
                    i_delta, j_delta = 0, 1
                # print('4')
        
    # print()

    res[m-1][n-1] = val

    for raw in res:
        print(*raw)
