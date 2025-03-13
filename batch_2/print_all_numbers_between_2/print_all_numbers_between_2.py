#input 2 numbers
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))

#generate numbers inbetween 2 numbers
for number in range(first_number + 1, second_number):
    #print numbers generated
    print(number)