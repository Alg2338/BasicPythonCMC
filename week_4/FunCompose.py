def compose(f, g):
    def h(*x):
        return f(g(*x), g(*x[::-1]))
    
    return h