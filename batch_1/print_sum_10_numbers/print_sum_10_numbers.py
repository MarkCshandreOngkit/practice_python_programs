#create function that ask number
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#call function 10 times
for i in range(10):
    number = ask()
    #add numbers each call
#print sum