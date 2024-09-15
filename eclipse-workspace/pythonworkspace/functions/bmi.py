def calculateBMI(height,weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi

print(calculateBMI(5.6, 74))