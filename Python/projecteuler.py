# 52

def check(a, b):
    a = str(a)
    b = str(b)
    aSet = set()
    bSet = set()
    for x in a:
        aSet.add(x)
    for x in b:
        bSet.add(x)
    return aSet == bSet

for i in range(1):
    if check(i, i*2) and check(i, i*3) and check(i, i*4) and check(i, i*5) and check(i, i*6):
        print(i)

# 53

import math
count = 0
for n in range(1, 100):
    for r in range(1, 100):
        if n > r:
            nfact = math.factorial(n)
            rfact = math.factorial(r)
            value = nfact / (rfact * math.factorial(n-r))
            if value > 1000000:
                count += 1
print(count)