#Find a string

def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            c += 1
    return c