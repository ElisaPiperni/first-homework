#The Captain's Room

k = int(raw_input())
rooms = map(int,raw_input().split())
s = set(rooms)
cap = (sum(s)*k - sum(rooms)) / (k-1)
print cap
