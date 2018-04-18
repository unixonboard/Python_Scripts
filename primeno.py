primecount=0
notprimecount=0

for var1 in range (2,101):
    isprime=True
    for var2 in range (2,var1-1):
        if var1%var2==0:
            print(var1,"its not Prime")
            isprime=False
            notprimecount=notprimecount+1
            break
    if isprime:
        print(var1,"its Prime No")
        primecount=primecount+1
print("=====================================")
print("Total No of Prime Count:",primecount)
print("Total No of Not Prime Count:",notprimecount)


