#Tuples

if __name__ == '__main__':
    n = int(raw_input())
    lst = map(int, raw_input().split())
    t = tuple(lst)
    print(hash(t))