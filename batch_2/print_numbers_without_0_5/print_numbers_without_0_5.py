#generate 0-100
for number in range(101):
    #check if number ends with 0 or 5
    if number % 5 != 0:
        #print number if true
        print(number)