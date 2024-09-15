# Python program to read
# json file
 
import json
import subprocess
import os

with open('/Users/thnanda/eclipse-workspace/pythonworkspace/hosts.json') as f:
    data= json.load(f)
    # print(f.read())
    # print(type(data))

lst = data
# print(lst)


g1=(lst[0])
print(type(g1))
for key, values in g1.items():
    print(f"{key}: {values}")

