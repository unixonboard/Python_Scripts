char=input()
if ord(char) >=65 and ord(char)<=90:
    print ("you have entered a uppercase")
    if char in ['A','E','I','O','U']:
        print ("You have entered a vowel")
    else:
        print ("you have entered a consonent")
elif ord(char)>=97 and ord(char)<=122:
    print ("you have entered lowercase:")
    if char in ['A','E','I','O','U']:
        print ("you have entered vowel:")
    else:
        print ("you have entered consonent:")
else:
    print ("youdidnt entered an alphabet")
               
               
