dict1={1:"john",2:"bob",3:"bill"}
print(dict1)

print(dict1.items())

print(dict1.keys())

k=dict1.keys()

for i in k:
    print(i)
    

for i in k:
    print(dict1[i])
    
v=dict1.values()
for i in v:print(i)

del dict1[2]

print(dict1)

