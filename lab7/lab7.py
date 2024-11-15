'''
####################################

    Savinova Alina Konstantinovna
    Group: U3745    Flow: 1.2
          Laboratory No. 7

####################################
'''
import Exercise.exerciseOne as one
import Exercise.exerciseTwo as two
import Exercise.exerciseThree as three

while True:
    print("Please select exercise (you should write number):")
    print("Exercise 1: Is it a literal crocodile or is it a 'cat'( :3 ) ?")
    print("Exercise 2: A counter or someone is counting sheep")
    print("Exercise 3: An editor's job in a company?...")
    print("Exercise 4: **Pouf**")
    print("0: If u want to exit the program")
    a = int(input('Write your choice in this -> '))
    match a:
        case 0:
            print('Bye bye :( ')
            break
        case 1:
            one.solution()
            print("\n\n")
        case 2:
            two.solution()
            print("\n\n")
        case 3:
            three.solution()
            print("\n\n")
        case 4:
            print("Look, focus: Task 4 disappear!\n**POUF**\n\n")
        case _:
            print("Ooops... u write not correct number\nPlease try again!\n\n")