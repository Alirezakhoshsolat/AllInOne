
def fibonacci ( NT , count=0 , n1 = 0 , n2 = 1 ):
   if NT <= 0:
      print("Please enter a positive integer")
   elif NT == 1:
      print("Fibonacci sequence up to",NT,":")
      print(n1)
   else:
      print("Fibonacci sequence:")
      while count < NT:
          print(n1)
          nth = n1 + n2
          n1 = n2
          n2 = nth
          count += 1

