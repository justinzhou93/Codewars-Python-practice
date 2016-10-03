def first_non_repeating_letter(string):
    #your code here
    print string
    list = [i.lower() for i in string]
    print list
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return string[i]
    return ""
