def duplicate_count(text):
    # Your code goes here
    mlist = []
    for i in range(len(text)):
        if text[i] in text[0:i]:
            if text[i] not in mlist:
                mlist.append(text[i])
    print len(mlist)

duplicate_count("Indivisibilities") 
