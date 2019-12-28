# Q3 Tables
#tables(3,10)
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# .
# .
# .
# 3 * 10 = 30

def tab(m, n):
    c = []
    for a in range(m, m+1):
        for i in range(1, n+1):
            b = a*i
            c.append(b)
    return c
