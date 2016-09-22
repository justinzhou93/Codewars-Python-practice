def digital_root1(n):
    # ...
    mstr = str(n)
    ans = 0
    while len(mstr) != 1:
        for i in range(len(mstr)):
            ans += int(mstr[i])
        mstr = str(ans)
        ans = 0
    print int(mstr)


digital_root1(16)