#Print parttens 

n = 5

for i in range(n):
    for j in range(i):
        print("* ",end="")
    print()


# nr = 8

for i in range(n):
    print(" "*(n-i),end="")
    print("* "*i)
    
    