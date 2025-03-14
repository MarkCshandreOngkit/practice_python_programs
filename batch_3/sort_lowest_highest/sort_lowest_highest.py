#create ask function(input number)
def ask():
    number = input("Input number({}): ".format(iteration))
    return number

#create function checks if input is digit/number or int
def check_digit(number):
    if number.isdigit():
        return True
    else:
        return False
    
#initialize
numbers = []
iteration = 0

#call function until invalid input(int is not inputted)(loop)
    #check if input is invalid, if true break loop
    #put the input in list
#sort list
#print list