import BMI
import Calculator
import two_pattern
import exam_planner
import fib
import guess
import hazine_sms
import maghloob
import string_to_dic
import corona_statistic_analyze
import word_count
import account


choice = int(input('''                                          **** welcome to my work ****
                   choose your service :
                   
                   1) BMI calculation.\t
                   2) Calculator.\t
                   3) play guess the number.\t
                   4) SMS cost.\t
                   5) for a cool number pattern.\t
                   6) for reversing your number.\t
                   7) for creating a Fibonacci sequence.\t
                   8) for counting letters in your text.\t
                   9) for planning your studies.\t
                   10) reviewing the corona statistic.\t
                   11) for counting words from a text file.\t
                   12) for creating and login to your account.\t'''))

#######BMI###########

if choice == 1 :
    weight = int(input("please enter your weight :"))
    height = float(input('please enter your height ; '))
    BMI.bmi(weight,height)

#######calculator######

elif choice == 2:
    cal_choice = int(input("""
                                    *****CALCULATOR MENU***
             choose function:
             1:ADD
             2:SUBTRACT
             3:MULTIPLICATION
             4:DIVISION2
             5:EXIT

             """))
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    Calculator.cal_menu(cal_choice, first_number,second_number)


#########guessing number game##########

elif choice == 3 :
    guess.guess_game()

########SMS cost######################

elif choice == 4 :
    yourSMS = str(input('please enter your SMS text : '))
    hazine = 100
    hazine_sms.sms_cost(yourSMS,hazine)

############patterns#################

elif choice == 5:
    pattern_choice=int(input('''***choose your desired patter***
            pattern 1
            pattern 2'''))
    if pattern_choice == 1:
        pattern_rows = int(input(" enter the number of rows: "))
        two_pattern.pattern1(pattern_rows)
    elif pattern_choice == 2:
        pattern_rows = int(input(" enter the number of rows: "))
        two_pattern.pattern2(pattern_rows)
    else:
        print('stay tune for new patterns')

###########reversing number############

elif choice == 6:
    number = int(input("Enter the number you want to reverse: "))
    maghloob.reversing_intiger(number)

###########fibonacci###################

elif choice == 7:
    number_of_terms = int(input("How many terms? "))
    fib.fibonacci(number_of_terms)


#############letter counting###########

elif choice == 8:
    text = str(input('please enter your desired text :'))
    string_to_dic.letter_count(text)


##########planning your studies#########

elif choice == 9:
    list_of_exam_days = []
    list_of_study_exam = []
    number_of_exams = int(input("Enter how many exams do you have : "))
    for i in range(0, number_of_exams):
        days = int(input('please enter your exam number '))
        list_of_exam_days.append(days)
    for j in range(0 , number_of_exams):
        study_days = int(input('please enter how many morning you should study for exam '))
        list_of_study_exam.append(study_days)
    exam_planner.pass_exam(list_of_exam_days , list_of_study_exam)


##########corona statistic############

elif choice == 10:
    corona_statistic_analyze.corona_statistic(a='WHO-COVID-19-Ir-data.csv')


#########word count##################

elif choice == 11:
    with open('text_file.txt' ) as text :
        file = text.read()
        word_count.word_count(file)

elif choice == 12:
    Stop=False
    account.account(Stop)


else :
    print(''' ******stay tuned for more and better works******
     *****thanks for your time*****''')







