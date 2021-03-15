import sys

print("BMICalculator.exe")
weight = input("Enter your weight in pounds: ")
height = input("Enter your height in inches: ")
heightF = float(height)
BMICalculator = round((703*float(weight)) / (heightF*heightF),2)
print("Your BMI is "+str(BMICalculator)+"%")