# Use python to implement you solution of choice to the computational problem. 
# Include as reasonable number of test to give confidence that your code is correct.

import pytest

# ---- Dynamic Programming Solution

# -- Least Common Prefix method
# input: beginning index for T1, beginning index for T2
# output: returns the length of the longest common prefix from the beginning indexes

def LCP(i, j, T1, T2):
    if (i <= j):
        return 0
    
    print(i, j)

def kLCSg(T1, T2, k):
    n = len(T1)
    m = len(T2)
    print('hello')
    

    for i in range(n):
        for j in range(m):

            option1 = max(i, j+1, k)

            option2 = max(i + 1, j, k)

            maximum = max(LCP(i, j) + (i + LCP(i, j), j + LCP(i, j), k - 1))

    return maximum



def evenMethod(num):
    return num % 2 == 0

def test_evenTest():
    assert evenMethod(22) == True
    with pytest.raises(AssertionError):
        assert evenMethod(7) == True
        
@pytest.fixture
def setup_kLCSg():
    T1 = "ACTAAT"
    T2 = "ACTAAG"
    k = 3
    
    return T1, T2, k
    
def test_LCP_ReturnsLengthZeroWhenijSame(setup_kLCSg):
    T1, T2, k = setup_kLCSg
    i = 3
    j = 3
    result = LCP(i, j, T1, T2)
    assert result == 0
    
def test_LCP_ReturnsLengthOneWhenijBeginning(setup_kLCSg):
    T1, T2, k = setup_kLCSg
    i = 0
    j = 0
    result = LCP(i, j, T1, T2)
    assert result == 0
    
    
# def test_kLCSg_returnsmax(setup_kLCSg):
#     T1, T2, k = setup_kLCSg
#     kLCSg()
