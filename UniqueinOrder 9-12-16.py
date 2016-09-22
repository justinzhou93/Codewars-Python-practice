def unique_in_order(iterable):
    mlist = []

    if len(iterable) == 1:
        print mlist.append(iterable[0])

    for i in range(len(iterable)):
        if iterable[i] != iterable[i-1]:
            mlist.append(iterable[i])
    print mlist

unique_in_order(['A', 'A'])