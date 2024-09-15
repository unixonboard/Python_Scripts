# n = int(input("Please Enter the number"))
#
# for i in range(n):
#     if ((i%10 == 0) & (i < 100)) :
#         continue
#     print(i)
#     else:
#         break


# n = int(input("Enter a number"))
#
# for i in range(2,n+1):
#
#     for j in range(2,i):
#
#         if(i % j == 0):
#
#             print("Not a Prime",i)
#
#             break
#
#     else:
#
#         print("prime",i)       

n =int(input("Enter an input"))
for i in range(n):
    if i<=100:
        if i%10 == 0:
            continue
        else:
            print(i)


   
