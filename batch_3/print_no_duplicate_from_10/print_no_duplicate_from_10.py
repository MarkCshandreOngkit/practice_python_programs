#create ask function(input number)
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#initialize list
unique_numbers = []
duplicate = []

#call function 10 times
for i in range(10):
    number = ask()
    #check if the number is not in the list
    if number not in unique_numbers and number not in duplicate:
        #put the number in list if true
        unique_numbers.append(number)

    #remove if there's a duplicate and put in duplicate list
    else:
        #checks if number in unique list
        if number in unique_numbers:
            #removes number from unique if true
            unique_numbers.remove(number)
        duplicate.append(number)
        

print(unique_numbers)


