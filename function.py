def ascii_weight(x):
    s = 0
    for i in x:
        n = ord(i)
        s = s + n
    return s

out = ascii_weight(34)
print(out)