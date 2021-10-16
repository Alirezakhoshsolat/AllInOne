
def bmi (H ,W):
    if H > 0 and H < 2.5:
        BMI=W / (H**2)
    else :
        H = H / 100
        BMI=W / (H**2)

    if BMI <= 18.5:
        print( "Underweight")
    elif BMI > 18.5 and BMI < 24.9:
        print("Normal weight ")
    elif BMI > 25 and BMI < 29.9:
        print("Overweight")
    else :
        print ("Obesity")
