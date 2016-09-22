def snail(array):
    length = len(array) - 1
    width = len(array[0])
    lpos = 0
    wpos = -1
    ans = []
    while length >= 0 and width > 0:
        if width > length:
            if wpos >= (len(array[0])) / 2:
                for i in range(width):
                    wpos -= 1
                    ans.append(array[lpos][wpos])
            else:
                for i in range(width):
                    wpos += 1
                    ans.append(array[lpos][wpos])
            width -= 1
        else:
            if lpos >= (len(array)) / 2:
                for i in range(length):
                    lpos -= 1
                    ans.append(array[lpos][wpos])
            else:
                for i in range(length):
                    lpos += 1
                    ans.append(array[lpos][wpos])
            length -= 1
    return ans


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print snail(array)