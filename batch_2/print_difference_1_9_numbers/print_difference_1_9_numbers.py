#create function that ask number
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#call function 10 times
for i in range(10):
    ask()
    #differentiate first number
    #subtract each numbers to first number each call
#print difference