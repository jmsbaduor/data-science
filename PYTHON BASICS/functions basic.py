# def james():
#     print("You are James")
#     print("And am You")
# print("This is outside the function")
# print(james())

# ---------------------------------------------------

# prompts for user input
value1 = input("What is your name?")
value2 = int(input("Enter your weight, Only numbers accepted"))
value3 = int(input("What is your height?"))

# bmi calculator function
def bmi_calculator(user_name, weight, height):
    bmi = weight / (height **2)
    print("bmi: ")
    print(bmi)
    if bmi > 25:
        return user_name + " is overweight"
    else:
        return user_name + " is not overweight"

# this will return the final result of the calculator
result = bmi_calculator(value1, value2, value3)
print(result)