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
iteration = 0
sum = 0

#call function until invalid input(int is not inputted)
while True:
    iteration += 1
    number = ask()
    #check if input is invalid, if true, iteration minus 1 and break loop
    check_input = check_digit(number)
    if check_input == False:
        iteration -= 1
        break
    number = int(number) #oh...
    #add number to sum
    sum += number

#sum divided by iteration 
average = sum / iteration

#print average
print(average)