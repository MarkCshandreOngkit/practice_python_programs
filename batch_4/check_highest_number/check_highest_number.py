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
highest_number = 0

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
    #check if number is greater than highest number
        #save number as highest number
#print highest number