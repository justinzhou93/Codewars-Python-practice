def maxSequence(arr):
	# ...
    li = 0
    lj = 0
    lamt = 0
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr) - i):
            temp += arr[i + j]
            if temp > lamt:
                lamt = temp
                li = i
                lj = i + j
        if lamt < temp:
            lamt = temp
    mlist = arr[li:lj+1]
    print mlist


maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])