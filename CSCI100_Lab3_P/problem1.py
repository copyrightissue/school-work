#Chris Rogers
prompt1 = 'Enter hours worked:\n'
hours = int(input(prompt1))
prompt2 = 'Enter pay rate:\n'
rate = int(input(prompt2))
regular = hours//40
overtimehours = hours%40
regularpay = 40 * rate
overtimerate = rate * 1.5
overtimepay = overtimehours * overtimerate
totalpay = overtimepay + regularpay
print ('Total Pay:',totalpay)




#print("Total Pay: " + str(pay))
