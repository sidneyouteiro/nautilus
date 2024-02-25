def questao3(p):
    l = len(p)
    if l < 1:
        return False
    for i in range(l):
        if p[i] != p[l-1-i]:
            return False
    return True
