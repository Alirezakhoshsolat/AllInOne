import ADD , sub
import multiply, divide

def cal_menu(cc ,fn ,sn) :

    if (cc==1):
            ADD.add(fn, sn)
    elif (cc==2):
           sub.subtract(fn, sn)
    elif (cc==3):
            multiply.multiply(fn, sn)
    elif (cc==4):
            divide.divide(fn, sn)
    elif (cc==5):
            return
    else:
        print( " your choice is not in menu ")
        



