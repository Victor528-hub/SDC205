from datetime import datetime

correct_number = 8
tries = 0

Name = input("What is your name? ")
StudentID = input("What is your studentID? ")

print(f"Hi {Name}! You are welcome to guess the number I am thinking of!")
current_time = datetime.now()
print("\nCurrent Date and Time:", current_time.strftime("%m/%d/%Y %I:%M%p"))
guess = int(input("Please guess a number between 1 and 10: "))
tries += 1

while guess != correct_number:

    if guess > correct_number:
        print("You guessed too high")
    else:
        print("You guessed too low")

    guess = int(input("Try again: "))
    tries += 1

print(f"Congratulations, {Name}! You guessed the number in {tries} tries!")

    
x = correct_number
count = 0
print("\nOutput from the 'while' loop: ")
while count < 8:
    count += 1
    x += 1
    print(f'{correct_number} incremented by {count} is {x}')
    count += 1

x = correct_number
print("\nOutput from the 'for' loop: ")
for count in range(1, 6):
    x += 1
    print(f'{correct_number} incremented by {count} is {x}')
    
