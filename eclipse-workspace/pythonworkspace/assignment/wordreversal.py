
s = "All the Power is with in you "
temp = s.split()
print(temp)
result=[]
i = len(temp)-1

print(i)

while i >= 0:
    result.append(temp[i])
    i-=1
print(result)

output = ' '.join(result)

print(output)