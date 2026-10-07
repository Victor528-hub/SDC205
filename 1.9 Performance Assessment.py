myName = input("Please enter your name: ")
myStudentID = input("Please enter your studentID: ")
number1=int(input("Please enter a whole number: "))
number2=int(input("Please enter a different second whole number: "))
answer1= number1 * number2
print (f'The result of {number1} time {number2} is: {answer1}')
answer2= number1 + number2
print (f'The result of {number1} plus {number2} is: {answer2}')
answer3= number1 - number2
print (f'The result of {number1} plus {number2} is: {answer3}')
if number1 > number2:
    print (f'Number1 is larger than Number2')
elif number1 < number2:
    print("Number2 is larger")
print(f'{myName}')
print(f'{myStudentID}')
