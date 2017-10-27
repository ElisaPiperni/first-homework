#Find the Second Largest Number

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m = max(arr)
    s_arr = set(arr)
    arr = list(s_arr)
    arr.remove(m)
    print max(arr)