#evaluate("32+")

def evaluate(s):
    list1 = []
    l = "0123456789"
    for i in s:
        if i in l:
            list1.append(int(i))
        else:
            if i == "+":
                a = list1.pop()
                b = list1.pop()
                c = int(a) + int(b)
                list1.append(c)
                
            elif i == "*":
                a = list1.pop()
                b = list1.pop()
                c = int(a) * int(b)
                list1.append(c)
                
            elif i == "-":
                a = list1.pop()
                b = list1.pop()
                c = int(a) - int(b)
                list1.append(c)
                
            else:
                a = list1.pop()
                b = list1.pop()
                c = int(a) // int(b)
                list1.append(c)
    return list1

#evaluate("32+")
#evaluate("32*")
#evaluate("34*62+12-3/")
#evaluate("22+2*34+6/")
#evaluate("22+2*34+6*")

