import sys

def v1(n):
    def multiply(x, res, res_size):
        carry = 0
        i = 0
        while i < res_size:
            prod = res[i] * x + carry
            res[i] = prod % 10
            carry = prod // 10
            i += 1
        while carry:
            res[res_size] = carry % 10
            carry //= 10
            res_size += 1
        
        return res_size
    res = [None] * 500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x += 1
    i = res_size - 1
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i -= 1

v1(5)