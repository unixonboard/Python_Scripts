s = "Take up one idea and make that idea your life."\
    "Think and dream of that idea and leave every other idea alone "
    
subs = "idea"
found = False
pos = -1
lenth = len(s)

while True:
    pos = s.find(subs, pos+1,lenth)
    if pos == -1:
        break
    print("Found the subs at pos",pos)
    found=True
if found == False:
    print("Not Found")
