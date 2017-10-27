#Capitalize!

def capitalize(string):
    l = string.split(" ")
    l1 =[]
    for i in l:
        w = i.capitalize()
        l1.append(w)
    string = " ".join(l1)
    return string