import math

def bmi_input(key = 1):
    user_weight = int(input("Please enter your weight: "))
    user_height = float(input("Please enter your height: "))
    
    if user_height == 0 or user_weight == 0:
        print("invalid weight or height")
        return
    
    bmi = key * (user_weight / (math.floor(math.pow(user_height,2))))

    if bmi < 18:
        print("You have a bmi of %d, so you are underweight." %(bmi))
    elif bmi > 25:
        print("You have a bmi of %d, so you are overweight." %(bmi))
    else:
        print("You have a bmi of %d, so you are normal weight" %(bmi))

def main():
    print("Hello and welcome to my BMI calculator!")
    print("Please select if you want to use the imperial system or the metric system")
    key = int(input("(input 0 for imperial, 1 for metric): "))
    
    if key == 0:
        bmi_input(703)
    elif key == 1:
        bmi_input()
    else:
        print("invalid selection")


if __name__ == '__main__':
    main()

'''
Output:


Hello and welcome to my BMI calculator!
Please select if you want to use the imperial system or the metric system
(input 0 for imperial, 1 for metric): 0
Please enter your weight: 200
Please enter your height: 70
You have a bmi of 28, so you are overweight.

Hello and welcome to my BMI calculator!
Please select if you want to use the imperial system or the metric system
(input 0 for imperial, 1 for metric): 1
Please enter your weight: 70
Please enter your height: 1.7
You have a bmi of 35, so you are overweight.

Hello and welcome to my BMI calculator!
Please select if you want to use the imperial system or the metric system
(input 0 for imperial, 1 for metric): 0
Please enter your weight: 0
Please enter your height: 0
invalid weight or height

Hello and welcome to my BMI calculator!
Please select if you want to use the imperial system or the metric system
(input 0 for imperial, 1 for metric): 7
invalid selection
'''
