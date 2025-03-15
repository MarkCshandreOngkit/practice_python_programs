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
highest_count = 0
most_duplicate = 0

#call function until invalid input(int is not inputted)
while True:
    iteration += 1
    number = ask()
    #check if input is invalid, if true break loop
    check_input = check_digit(number)
    if check_input == False:
        break
    number = int(number)
    #put input in numbers
    numbers.append(number)

#iterate through each number
for number in numbers:
    #count the times the number appeared in the list
    count = numbers.count(number)
    #check if the current count is higher than the previous count
    if count > highest_count:
        #save the number as most duplicate
        highest_count = count
        most_duplicate = number

#print most duplicate
print(most_duplicate)


