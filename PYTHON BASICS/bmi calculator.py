name = input("What is your name? ")

height_m = 4
weight_kg = 24

bmi = weight_kg / (height_m * height_m)


print("your BMI is ")
print(bmi)

if bmi < 25:
    print(name + ", You are not overweight")
else:
    print(name + ", You are overweight")
