#function that ask number
def ask():
    number = int(input("Input number({}): ".format(i + 1)))
    return number

#initialize even counter
even_counter = 0

#call function 10 times
for i in range(10):
    number = ask()
    #check if number is even
        #add 1 to even counter if true
#print even counter