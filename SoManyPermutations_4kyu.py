import math

def permutations(s):
    res = []
    n = len(s)  
    cells = len(s)
    total = math.factorial(n) // math.factorial(n - cells)
    
    for i in range(total):
        perm = []
        source = list(range(n)) 
        for j in range(cells):
            block_size = math.factorial(cells - 1 - j)
            idx = (i // block_size) % len(source)
            perm.append(source[idx])
            source.pop(idx)
        
        perm_string = ''.join([s[idx] for idx in perm])
        res.append(perm_string)
    
    unique = []
    seen = set()
    for p in res:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    
    return unique