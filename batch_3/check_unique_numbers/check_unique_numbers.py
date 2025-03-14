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

#initialize unique and duplicate list
unique_numbers = []
duplicate = []
iteration = 0

#call function until invalid input(int is not inputted)
while True:
    iteration += 1
    number = ask()
    #check if input is valid, if true break loop
    check_input = check_digit(number)
    if check_input == False:
        break
    int(number)
    
    #check if the number is not in unique and duplicate
    if number not in unique_numbers and number not in duplicate:
        #put the number in unique if true
        unique_numbers.append(number)

    #remove if there's a duplicate and put in duplicate list
    else:
        #put the number in duplicate
        duplicate.append(number)
        #check if number in unique list
        if number in unique_numbers:
            #removes number from unique if true
            unique_numbers.remove(number)
        
#iterate through each unique
for unique_number in unique_numbers:
    #print unique number and "Unique"
    print(f'{unique_number}, "Unique"')
#iterate through each duplicate
for duplicate_number in duplicate:
    #print duplicate number and "Duplicate"
    print(f'{duplicate_number}, "Duplicate"')            
