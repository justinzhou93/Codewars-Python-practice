def make_smallest(n, front):
    m = []
    ans = ""
    for i in range(len(str(n))-front):
        m.append(str(n)[len(str(n))-i-1])
    m.sort()
    for k in range(len(m)):
        ans += m[k]
    return int(str(n)[:front] + ans)

def next_bigger(n):
    #your code here
    m = []
    ans = ""
    for i in range(len(str(n))):
        m.append(str(n)[i])
    for i in range(len(m)-1):
        smallest = 9
        sj = 0
        if m[len(m)-i-2] < m[len(m)-i-1]:
            for j in range(i+1):
                if int(m[len(m) - i - 1 + j]) < smallest and int(m[len(m) - i - 1 + j]) > int(m[len(m)-i-2]):
                    smallest = m[len(m) - i - 1 + j]
                    sj = j
            m[len(m)-i-2], m[len(m)-i-1+sj] = m[len(m)-i-1+sj], m[len(m)-i-2]
            for k in range(len(m)):
                ans += m[k]
            return make_smallest(int(ans), len(m)-i-1)

    return -1


#print make_smallest(1234567980, 8)
print next_bigger(294173) 
