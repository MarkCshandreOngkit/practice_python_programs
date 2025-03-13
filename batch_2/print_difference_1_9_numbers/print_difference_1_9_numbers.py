#create function that ask number
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#call function 10 times
for i in range(10):
    #differentiate first number
    if i == 0:
        first_number = ask()
        print("First Number")
    else:
        number = ask()
    #subtract each numbers to first number each call
    first_number -= number
    
#print difference