from prime import prime_number

def test_prime_even():
    assert prime_number(2) == True
    for i in range(4, 100, 2):
        assert prime_number(i) == False
        
def test_prime_odd():
    for i in [3,5,7,11,13]:
        assert prime_number(i) == True
    for i in [9,15,35,121]:
        assert prime_number(i) == False
        
