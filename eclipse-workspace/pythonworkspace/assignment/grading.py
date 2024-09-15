m,p,c=[int(mark) for mark in input("Enter marks for maths, physics, chemsitry:").split()]

avg = (m+p+c)/3
# print(avg)

if m < 35 or p<35 or c<35:

    print("Failed")

elif avg<=50:

    print("Grade is C")

elif avg<=69:

    print("Grade is B")

else:

    print("Grade A")