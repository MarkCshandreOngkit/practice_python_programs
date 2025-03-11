#function that ask number
def ask():
    num = int(input("Input number({}): ".format(i + 1)))
    return num

#initialize odd counter
odd_counter = 0

#call function 10 times
for i in range(10):
    number = ask()
    #check if number is odd
    if number % 2 == 1:
        #add 1 to odd counter if true
        odd_counter += 1

#print odd counter
print(odd_counter)