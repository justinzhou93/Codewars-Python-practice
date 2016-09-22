def lcs1(x, y):
  '''TODO'''
  mlist = []
  xlcs = ""
  ylcs = ""
  last = 0
  for i in range(len(x)):
      for j in range(len(y[last:])):
          if x[i] == y[j + last - 1]:
              last = j
              xlcs += x[i]
  last = 0
  for i in range(len(y)):
      for j in range(len(x[last:])):
          if y[i] == x[j + last - 1]:
              last = j
              ylcs += y[i]
  if len(xlcs) > len(ylcs):
      print xlcs
  else:
      print ylcs


def xlcs(x, y):
    xans = ""
    if len(x) == 0:
        return xans
    elif len(x) == 1:
        for i in range(len(y)):
            if x[0] == y[i]:
                xans += y[i]
        return xans
    else:
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    return x[i] + xlcs(x[i+1:], y[j+1:])
        return xans

def ylcs(y, x):
    xans = ""
    if len(y) == 0:
        return xans
    elif len(y) == 1:
        for i in range(len(x)):
            if y[0] == x[i]:
                xans += x[i]
        return xans
    else:
        for i in range(len(y)):
            for j in range(len(x)):
                if y[i] == x[j]:
                    return y[i] + ylcs(y[i+1:], x[j+1:])
        return xans

def lcs(x, y):

    if len(xlcs(x, y)) > len(ylcs(y, x)):
        print xlcs(x, y)
    else:
        print ylcs(y, x)


lcs("" , "")