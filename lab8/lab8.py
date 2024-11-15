'''
####################################

    Savinova Alina Konstantinovna
    Group: U3175    Flow: 1.2
          Laboratory No. 8

####################################
'''
import Exercise.exerciseOne as one
import Exercise.exerciseTwo as two
import Exercise.exerciseThree as three
import Exercise.exerciseFour as four
import Exercise.exerciseFive as five

while True:
    print("Please select exercise (you should write number):")
    print("Exercise 1: Please click me!")
    print("Exercise 2: Say Hello! My friend!")
    print("Exercise 3: Calculator!")
    print("Exercise 4: Currency Converter")
    print("Exercise 5: Tic Tac Toe")
    print("0: If u want to exit the program")
    a = int(input('Write your choice in this -> '))
    match a:
        case 0:
            print('Bye bye :( ')
            break
        case 1:
            one.solve()
            print("\n\n")
        case 2:
            two.solve()
            print("\n\n")
        case 3:
            three.solve()
            print("\n\n")
        case 4:
            four.solve()
            print("\n\n")
        case 5:
            five.solve()
            print("\n\n")
        case _:
            print("Ooops... u write not correct number\nPlease try again!\n\n")