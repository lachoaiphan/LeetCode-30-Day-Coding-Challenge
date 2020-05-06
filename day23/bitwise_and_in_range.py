"""
Prompt:
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""

# Runs in O(log n) and O(1) space. Implemented an algorithm involving comparing the numbers' two most significant figures


def mostSigFig(num):
    position = 0
    while num >= 1:
        num = num >> 1
        position += 1
    return position


def rangeBitwiseAnd(m, n):
    m_sig = mostSigFig(m)
    n_sig = mostSigFig(n)
    result = 0
    while m_sig == n_sig and (m > 0 and n > 0):
        sig_value = pow(2, m_sig - 1)
        result += sig_value
        m = m - sig_value
        n = n - sig_value
        m_sig = mostSigFig(m)
        n_sig = mostSigFig(n)
    return result


# Test Case
print(rangeBitwiseAnd(5, 7))  # print 4
