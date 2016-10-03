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
            return [i+1, counts]
        elif formula[i] == "(" or formula[i] == "[" or formula[i] == "{":
            temp = parse_molecule(formula[i+1:])
            i += temp[0]
            if i+1 < len(formula):
                if formula[i+1].isdigit()==True:
                    i+=1
                    for key, value in temp[1].items():
                        temp[1][key] = value * int(formula[i])
            counts = combine(temp[1], counts)
        else:
            if formula[i].isupper()==True:
                if i+1 < len(formula):
                    if formula[i+1].islower()==True:
                        if formula[i:i+2] in counts:
                            counts[formula[i:i+2]]+=1
                            last = formula[i:i+2]
                            i+=1
                        else:
                            counts[formula[i:i+2]] = 1
                            last = formula[i:i+2]
                    else:
                        if formula[i] in counts:
                            counts[formula[i]] = 1
                            last = formula[i]
                        else:
                            counts[formula[i]] = 1
                            last = formula[i]
                else:
                    if formula[i] in counts:
                        counts[formula[i]] = 1
                        last = formula[i]
                    else:
                        counts[formula[i]] = 1
                        last = formula[i]
        i += 1
    return counts
