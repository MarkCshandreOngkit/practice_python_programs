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
        ask()
    #subtract each numbers to first number each call
#print difference