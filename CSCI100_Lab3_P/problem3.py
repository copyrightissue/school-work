#Chris Rogers
num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))
num3 = float(input('Enter third number:'))
if num1> num2 and num1>num3:
    print ('Largest number:',num1)
elif num2 > num3:
        print ('Largest number:',num2)
else: print ('Largest number:',num3)
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('mediumest number',num2)
    else:
        print ('mediumest number',num3)
else: print ('mediumest number',num1)
if num1< num2 and num1<num3:
    print ('smallest number:',num1)
elif num2 < num3:
        print ('smallest number:',num2)
else: print ('smallest number:',num3)



#if num2 > num3 and num2 < num1:
 #   print('Second largest number:',num2)
#else:
 #   if num1 > num2 and num1 < num3:
  #          print ('Second largest number',num3)
   # else: print ('Second largest number',num1)

#print(num1)
