#create ask function(input number)
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#initialize list
unique_numbers = []

#call function 10 times
for i in range(10):
    number = ask()
    
    #check if the number is not in the list
        #put the number in list if true
