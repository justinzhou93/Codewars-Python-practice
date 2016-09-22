def dirReduc(arr):
    if len(arr) == 1 or conflicts(arr) == -1:
        return arr
    else:
        index = int(conflicts(arr))
        del arr[index:index+2]
        return dirReduc(arr)


def conflicts(arr):
    for i in range(len(arr) - 1):
        if arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
            return int(i)
        elif arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
            return int(i)
        elif arr[i] == "EAST" and arr[i + 1] == "WEST":
            return int(i)
        elif arr[i] == "WEST" and arr[i + 1] == "EAST":
            return int(i)
    else:
        return -1

print dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) 
