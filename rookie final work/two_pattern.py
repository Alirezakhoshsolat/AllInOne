

def pattern1 (rows):
    for i in range (1 , rows +1):
        val = i
        dif = rows - 1
        print (val, end = "  " )
        for j in range (1 , i) :
            val += dif
            dif = dif - 1
            print ( val , end = "  ")
        print()
            
def pattern2(r):
    val = 1
    dif = 0
    for i in range (0 , r+1):
        for n in range ( 1 , i +1):
            val= dif + val
            dif += 1
            print (val , end = "  " )
        print ()




        
               

               
               
               
    
