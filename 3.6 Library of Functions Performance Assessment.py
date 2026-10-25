def functionOne():
    print("My Student ID is stealbb9443")

def functionTwo():
    var1 = int(input("Please enter a number: "))
    var2 = int(input("Please enter a number: "))
    answer = var1 + var2
    print(f'The sum of {var1} and {var2} is {answer}')
    return answer

def functionThree(answer):
    if answer >= 5:
        print("The sum is greater than 5")
    else:
        print("The sum is 5 or less")

    return 9443

def main():
    # Call functionOne to display the Student ID
    functionOne()

    # Call functionTwo and store the returned sum
    sumValue = functionTwo()

    # Pass the sum to functionThree and store the returned Student ID Number
    studentIdNumber = functionThree(sumValue)

    # Display the value returned from functionThree
    print(f'functionThree returned the value of {studentIdNumber}')
    
main()



    
