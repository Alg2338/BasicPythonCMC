def sheff(A, B):
    return (not A and not B) or (not(A and B) and (A or B))