#create ask function(input number)
def ask():
    number = input("Input number({}): ".format(iteration))
    return number

#create function checks if input is digit/number
def check_digit(number):
    if number.isdigit():
        return True
    else:
        return False
    
#initialize
numbers = []
iteration = 0

#call function until invalid input(int is not inputted)
while True:
    iteration += 1
    number = ask()
    #check if input is invalid, if true break loop
    check_input = check_digit(number)
    if check_input == False:
        break
    int(number)
    #put input in numbers
    numbers.append(number)
    
#iterate through each number
    #count the times the number appeared in the list
    #check if the current count is higher than the previous count
        #save the number as most duplicate
#print most duplicate


