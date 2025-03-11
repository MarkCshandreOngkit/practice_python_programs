#generate 0-100
for number in range(101):
    #check if number ends with 0
    if "0" not in str(number):
        #print number if true
        print(number)