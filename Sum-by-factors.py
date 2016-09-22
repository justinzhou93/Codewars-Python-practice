def prime_factors(n):
    i = 2
    factors = []
    if n < 0:
        n *= -1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def combine(arr1, arr2):
    for a in arr1:
        if not a in arr2:
            arr2.append(a)
    return arr2

def sum_for_list(lst):
    #....
    factors = []
    sums = []
    for i in range(len(lst)):
        combine(prime_factors(lst[i]),factors)
    for i in range(len(factors)):
        msum = 0
        for j in range(len(lst)):
            if not lst[j]%factors[i]:
                msum += lst[j]
        sums.append([factors[i], msum])
    sums.sort(key=lambda factors:factors[0])
    return sums