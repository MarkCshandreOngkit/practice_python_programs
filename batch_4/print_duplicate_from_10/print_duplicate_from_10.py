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
        #put the number in unique if true
    #remove in unique if there's a duplicate and put in duplicate list
        #checks if number in unique list
            #removes number from unique if true
#print duplicate