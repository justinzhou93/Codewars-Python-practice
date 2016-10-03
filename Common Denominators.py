def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def lcmapp(lst):
    if len(lst) == 2:
        return lcm(lst[0], lst[1])
    else:
        return lcm(lst[0], lcmapp(lst[1:]))

def convertFracts(lst):
    denom = [i[1] for i in lst]
    ans = []
    lcm = lcmapp(denom)
    for i in range(len(lst)):
        ans.append([lcm/denom[i]*lst[i][0],lcm])
    return ans
