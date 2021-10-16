
def reversing_intiger ( original_number , revers_number = 0 ):
    while (original_number > 0):
        remainder = original_number % 10
        revers_number = (revers_number * 10) + remainder
        original_number = original_number // 10
    print("The reverse number is : ", revers_number)
