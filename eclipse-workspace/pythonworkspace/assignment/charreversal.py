
s = "python is cool"

temp = s.split()
print("Temp=",temp)

print(len(temp))

result=[]

i = 0

while i < len(temp):
    result.append(temp[i] [::-1])
    i+=1
print(result)

output1 = ' '.join(result)
print(output1)