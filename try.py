def something(val):
    return ord(val)


s = ['a', 'd', 'b', 'c', 'o', 'i', 'e']

print sorted(s, key=lambda x:something(x))
print ord('a'), ord('o')