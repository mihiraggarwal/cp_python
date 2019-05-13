# The user chooses if it wants to solve sums or ask questions. Four basic operations to be used

import random
print("Let's do math")
print('Do you wanna solve sums? (Yes/No)')
choiceOfQprev=input()
choiceOfQ=choiceOfQprev.lower() and choiceOfQprev.capitalize()
try:
    if choiceOfQ=='Yes':
        print('Do you want to do addition, subtraction, multiplication or division?')
        typeOfQprev=input()
        typeOfQ=typeOfQprev.lower() and typeOfQprev.capitalize()
        firstNumber=random.randint(1, 101)
        secondNumber=random.randint(1, 101)
        if typeOfQ=='Addition':
            print('{} + {} =?'.format(firstNumber, secondNumber))
            answer1=int(input())
            if answer1==firstNumber+secondNumber:
                print('The answer is correct')
            else:
                while answer1!=firstNumber+secondNumber:
                    print('The answer is wrong, please try again')
                    answer1=int(input())
                    if answer1==firstNumber+secondNumber:
                        print('The answer is correct')
        elif typeOfQ=='Subtraction':
            print('{} - {} =?'.format(firstNumber, secondNumber))
            answer2=int(input())
            if answer2==firstNumber-secondNumber:
                print('The answer is correct')
            else:
                while answer2!=firstNumber-secondNumber:
                    print('The answer is wrong, please try again')
                    answer2=int(input())
                    if answer2==firstNumber-secondNumber:
                        print('The answer is correct')
        elif typeOfQ=='Multiplication':
            print('{} * {} =?'.format(firstNumber, secondNumber))
            answer3=int(input())
            if answer3==firstNumber*secondNumber:
                print('The answer is correct')
            else:
                while answer3!=firstNumber*secondNumber:
                    print('The answer is wrong, please try again')
                    answer3=int(input())
                    if answer3==firstNumber*secondNumber:
                        print('The answer is correct')
        elif typeOfQ=='Division':
            print('{} / {} =?'.format(firstNumber, secondNumber))
            print('Round the answer to the integer before it')
            answer4=int(input())
            if answer4==int(firstNumber/secondNumber):
                print('The answer is correct')
            else:
                while answer4!=int(firstNumber/secondNumber):
                    print('The answer is wrong, please try again')
                    answer4=int(input())
                    if answer4==int(firstNumber/secondNumber):
                        print('The answer is correct')
        else:
            print('Please choose between addition, subtraction, multiplication and division')
    elif choiceOfQ=='No':
        print('Do you wanna ask a question? (Yes/No)')
        choiceOfQ2prev=input()
        choiceOfQ2=choiceOfQ2prev.lower() and choiceOfQ2prev.capitalize()
        if choiceOfQ2=='Yes':
            print('Enter the first number')
            firstNumber2=int(input())
            print('Enter the second number')
            secondNumber2=int(input())
            print('What operation do you want to perform? (addition, subtraction, multiplication, division)')
            operationPrev=input()
            operation=operationPrev.lower() and operationPrev.capitalize()
            if operation=='Addition':
                print(firstNumber2+secondNumber2) 
            elif operation=='Subtrction':
                print(firstNumber2-secondNumber2)
            elif operation=='Multiplication':
                print(firstNumber2*secondNumber2)
            elif operation=='Division':
                print(firstNumber2/secondNumber2)
            else:
                print('Please choose between addition, subtraction, multiplication, division')
        elif choiceOfQ2=='No':
            print("I'm sorry, we can't help you")
        else:
            print('Please choose between Yes and No')
    else:
        print('Please choose between Yes and No')
except ValueError:
    print('Please enter an integer')
