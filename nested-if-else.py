char=input()
if ord(char)>=65 and ord(char)<=90:
    print("its Uppercase")
    if char in ['A','E','I','O','U']:
        print("Its vowel")
    else:
        print("its Consonant")
elif ord(char)>=97 and ord(char)<=122:
    print("its lowercase")
    if char in ['a','e','i','o','u']:
        print("its vowel")
    else:
        print("its consonant")
else:
    print("you have not entered a letter")
    
    
    
