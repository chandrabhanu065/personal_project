import pytest


#def input_value():
input =  [(1,2,3),(4,5,6)]

@pytest.mark.parmeterize("a,b,c",input)
def test_even(a,b,c):
    print(a)
    print(b)
    print(c)