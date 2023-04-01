weight = float(input())
height = float(input())
BMI = weight / (height * height)

if BMI <= 18.5:
    print("Underweight")
if BMI > 18.5 and BMI < 25:
    print("Normal weight")
if BMI >= 25:
    print("Overweight")