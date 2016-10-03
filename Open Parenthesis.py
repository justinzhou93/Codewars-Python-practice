def is_balanced(source, caps):
    mstack = []
    same = False
    for i in range(len(caps)):
        if caps.count(caps[i]) > 1:
            same = True
    for i in range(len(source)):
        if source[i] in caps:
            if same:
                if len(mstack) > 0:
                    if mstack[len(mstack) - 1] == source[i]:
                        mstack.pop()
                    else:
                        mstack.append(source[i])
                else:
                    mstack.append(source[i])
            else:
                if caps.index(source[i]) % 2 == 0:
                    mstack.append(source[i])
                else:
                    if len(mstack) > 0:
                        if mstack[len(mstack) - 1] == caps[caps.index(source[i]) - 1]:
                            mstack.pop()
                        else:
                            print 2
                            return False
                    else:
                        return False
    if len(mstack) > 0:
        return False
    return True
