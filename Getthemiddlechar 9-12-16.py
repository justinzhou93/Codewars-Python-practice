def get_middle(s):
    #your code here
    length = len(s)
    if len(s)%2 == 0:
        print s[length/2-1] + s[length/2]
    elif length%2 == 1:
        print s[length/2]


def get_middle1(s):
   print s[(len(s)-1)/2:len(s)/2+1]

get_middle1("aba")