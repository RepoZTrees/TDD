
def prime_number(n):
    if n%2 == 0: # for e.g.4%2=0(4/2=remainder0) Or 5%2=1(5/2= remainder1)
        return n == 2
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
