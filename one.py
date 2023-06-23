#BMI App (beginner's version) Weight/Height*Height

weight = int(input("Please enter your weight in kgs: "))

height_cm = int(input("Please enter your height in centimeters: "))

#convert height in centimeters to meters

height_m = height_cm/100

#Calculate BMI

bmi = weight/(height_m**2)

#If your BMI is less than 18.5, it falls within the underweight range.
#If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
#If your BMI is 25.0 to 29.9, it falls within the overweight range.
#If your BMI is 30.0 or higher, it falls within the obese range.


try:
    if bmi < 18.5:
        print("You are within the underweight range")
    elif bmi == 18.5 or bmi < 25:
        print("You are withing the healthy range!")
    elif bmi == 25 or bmi < 30:
        print("You are within the overweight range")
    elif bmi >= 30:
        print("You are within the obese range!")
    else:
        print("See your doctor urgently")
        
except ZeroDivisionError:
    print("You cannot divide by zero")

finally:
    print("BMI is a great way to track your health!")