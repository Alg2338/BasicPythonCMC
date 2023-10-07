def det4(*matrix):
    matrix = list(map(list, matrix))
    
    def det_n(matrix, n, used_col, i):
        if i == n - 1:
            j = 0
            while used_col[j]:
                j += 1
            
            deg = 0
            for k in range(j + 1, n):
                deg += used_col[k]
            return (-1)**deg * matrix[i][j]
        
        res = 0
        j = 0
        while (j < n):
            if not used_col[j]:
                used_col[j] = True
                
                deg = 0
                for k in range(j + 1, n):
                    deg += used_col[k]

                res += (-1)**deg * matrix[i][j] *  det_n(matrix, n, used_col, i + 1)
                used_col[j] = False

            j += 1
        
        return res
    
    n = len(matrix)
    return det_n(matrix, n, [False] * n, 0)
