import math
predel = int(input())
for m in range(2, predel):
    for n in range(1, m):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if c <= predel and math.gcd(a, b, c) == 1:
            if a > b:
                a, b = b, a
            print(a, b, c)