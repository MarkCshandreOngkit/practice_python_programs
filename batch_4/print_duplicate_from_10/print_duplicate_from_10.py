#create ask function(input number)
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#initialize lists
unique_numbers = []
duplicates = []

#call function 10 times
for i in range(10):
    number = ask()

    #check if the number is not in unique and duplicate
    if number not in unique_numbers and number not in duplicates:
        #put the number in unique if true
        unique_numbers.append(number)

    #remove in unique if there's a duplicate and put in duplicate list
    else:
        #checks if number in unique list
        if number in unique_numbers:
            #removes number from unique if true
            unique_numbers.remove(number)
        duplicates.append(number)

#print duplicate
print(duplicates)