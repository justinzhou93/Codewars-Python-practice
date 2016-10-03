def combine(dict1, dict2):
    for i in dict2:
        if i in dict1:
            dict1[i] += dict2[i]
        else:
            dict1[i] = dict2[i]
    return dict1

def parse_molecule (formula):
    counts = {}
    last = ""
    i=0
    while i < len(formula):
        print formula[i] + ": " + str(i)
        print counts
        if formula[i].isdigit() == True:
            if i + 1 < len(formula):
                if formula[i + 1].isdigit() == True:
                    counts[last] += int(formula[i:i+2]) - 1
                    i+=1
                else:
                    counts[last] += int(formula[i])-1
            else:
                counts[last] += int(formula[i]) - 1
        elif formula[i] == ")" or formula[i] == "]" or formula[i] == "}":
            print 2
            return [i+1, counts]
        elif formula[i] == "(" or formula[i] == "[" or formula[i] == "{":
            print 3
            temp = parse_molecule(formula[i+1:])
            i += temp[0]
            if i+1 < len(formula):
                if formula[i+1].isdigit()==True:
                    i+=1
                    for key, value in temp[1].items():
                        temp[1][key] = value * int(formula[i])
            counts = combine(temp[1], counts)
        else:
            print 4
            if formula[i].isupper()==True:
                if i+1 < len(formula):
                    print "a"
                    if formula[i+1].islower()==True:
                        if formula[i:i+2] in counts:
                            counts[formula[i:i+2]] += 1
                            last = formula[i:i+2]
                            i+=1
                        else:
                            counts[formula[i:i+2]] = 1
                            last = formula[i:i+2]
                    else:
                        if formula[i] in counts:
                            counts[formula[i]] += 1
                            last = formula[i]
                        else:
                            counts[formula[i]] = 1
                            last = formula[i]
                else:
                    if formula[i] in counts:
                        counts[formula[i]] += 1
                        last = formula[i]
                    else:
                        counts[formula[i]] = 1
                        last = formula[i]
        i += 1
    return counts


import re


def parse_molecule1(formula):
    f = formula
    f = re.sub('[\[\{]', '(', f)
    f = re.sub('[\]\}]', ')', f)

    # Tokenizer
    n = len(f)
    a = []
    i = 0
    while i < n:
        if f[i].isupper():
            a.append(f[i])
            i += 1
        elif f[i].islower():
            a[-1] += f[i]
            i += 1
        elif f[i].isdigit():
            val = 0
            while i < n and f[i].isdigit():
                val = val * 10 + ord(f[i]) - ord('0')
                i += 1
            a.append(val)
        else:
            a.append(f[i])
            i += 1
    res = [{}]
    n = len(a)
    i = 0
    while i < n:
        if re.match(r'^[A-Z][a-z]?$', a[i]):
            elem = a[i]
            if i + 1 < n and isinstance(a[i + 1], int):
                cc = a[i + 1]
                i += 2
            else:
                cc = 1
                i += 1
            if not elem in res[-1]:
                res[-1][elem] = cc
            else:
                res[-1][elem] += cc
        elif a[i] == '(':
            res.append({})
            i += 1
        elif a[i] == ')':
            if i + 1 < n and isinstance(a[i + 1], int):
                cc = a[i + 1]
                i += 2
            else:
                cc = 1
                i += 1
            for k in res[-1]:
                if not k in res[-2]:
                    res[-2][k] = cc * res[-1][k]
                else:
                    res[-2][k] += cc * res[-1][k]
            res.pop()
    return res.pop()



print parse_molecule("(C5H5)Fe(CO)2CH3")


