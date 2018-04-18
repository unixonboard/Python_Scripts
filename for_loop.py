count=0
print("Enter your Name:")
name = input()
for letter in name :
    if(letter in ['A','E','I','O','U','a','e','o','u']):
        count=count+1
print ("you have ", count, "vowels.")
