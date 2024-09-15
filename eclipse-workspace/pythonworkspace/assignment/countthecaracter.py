''''s = 'asssssjjduehfkkiuuuhfhfndmdkddaiyryryfhff'
d = {}
for c in s:
    if c in d.keys():
        d[c] = d[c]+1
        print(d)
    else:
        d[c] = 1
        # print(d)
        
for k,v in d.items():
    print("{} = {} times ".format(k,v))'''
    
