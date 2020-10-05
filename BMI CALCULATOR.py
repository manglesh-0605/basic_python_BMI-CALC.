print('THIS IS A  BMI CALCULATOR')
weight=float(input('Enter your weight in kg\n'))
height=float(input('Enter your height in meters\n'))
bmi=weight/(height**2)
print(f'your BMI is {bmi}')
if bmi<18.5:
    print('you are underweight')
elif bmi>=18.5 and bmi<=29.9:
    print('your BMI is normal you are in healthy weight range')
elif bmi>29.9:
    print('you are overweight')
else:
    print('Enter the valid input')

