print("This is a B.M.I calculator.")

weight = float(input("Enter your weight(in kgs): "))
height = float(input("Enter your height(in m): "))


def bmi_calculator():
    bmi = weight / (height * height)

    if bmi < 18.5:
        print("You are underweight")

    if 25 > bmi > 18.5:
        print("You are normal and healthy")

    if bmi > 25:
        print("You are overweight")


bmi_calculator()
