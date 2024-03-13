from gmpy import invert, mpz


def dlog(p, g, h, B):
    left = {(h * invert(pow(g, x1, p), p)) % p: x1 for x1 in xrange(B)}
    g_b = pow(g, B, p)
    for x0 in xrange(B):
        value = pow(g_b, x0, p)
        if value in left:
            return x0, left[value]
    return None


p = input('Enter prime  :  ')
g = input('Enter g      :  ')
h = input('Enter h      :  ')
base = input('Enter base of B : ')
power = input('Enter power of B: ')
p = mpz(p)
g = mpz(g)
h = mpz(h)
B = mpz(base ** power)
x = dlog(p, g, h, B)
print('x0 = ' + str(x[0]))
print('x1 = ' + str(x[1]))
print('x = ' + str((x[0] * B + x[1])))
