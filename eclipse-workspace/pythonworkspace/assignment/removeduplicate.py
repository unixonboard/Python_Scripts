s = "aaasdfjoKASGGGHSKKKDIEJMMkksdfkdsijDNF"
print(len(s))
temp = []

for c in s:
    if c not in temp:
        temp.append(c)
print(temp)
print(len(temp))

op=''.join(temp)
print(op)