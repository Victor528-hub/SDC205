from datetime import datetime

correctNumber = 8
numberOfTries = 0

studentName = input("What is your name? ")
studentId = input("What is your studentID? ")

print(f'\nStudentID: {studentId}')
print(f"Hi {studentName}! You are welcome to guess the number I am thinking of!")
current_time = datetime.now()
print("\nCurrent Date and Time:", current_time.strftime("%m/%d/%Y %I:%M%p"))
guess = int(input("Please guess a number between 1 and 10: "))
numberOfTries += 1

while guess != correctNumber:

    if guess > correctNumber:
        print("You guessed too high")
    else:
        print("You guessed too low")

    guess = int(input("Try again: "))
    numberOfTries += 1

print(f"Congratulations, {studentName}! You guessed the number in {numberOfTries} tries!")

    
x = correctNumber
count = 0
print("\nOutput from the 'while' loop: ")
while count < 5:
    count += 1
    x += 1
    print(f'{correctNumber} incremented by {count} is {x}')
    

x = correctNumber
print("\nOutput from the 'for' loop: ")
for count in range(1, 6):
    x += 1
    print(f'{correctNumber} incremented by {count} is {x}')
    
