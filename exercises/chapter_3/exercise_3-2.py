
weight = float(input("Type your weight in kilograms:\n"))
height = float(input("Type your height in meters:\n"))
bmi = weight / (height * height)

print("%.2f" % bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 < bmi <= 24.9:
    print("Normal weight")
elif 25.0 < bmi < 29.9:
    print("Overweight")
elif bmi > 30:
    print("Obesity")
