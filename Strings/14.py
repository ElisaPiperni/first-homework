#Merge the Tools!

def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        t = string[i:i+k]
        u=''
        for j in range(len(t)):
            if t[j] not in u:
                u +=t[j]
        print u