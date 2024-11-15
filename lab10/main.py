from Exercise import exercise8 as eight, exercise9 as nine, exercise7 as seven

info = '''Напишите число, которое соответствует заданию из списка:
\t1. Упражнение 7
\t2. Упражнение 8
\t3. Упражнение 9
\t0. Выход'''
while True:
     print(info)
     a = input('Пожалуйста введите число: ')
     match a:
         case '1':
             seven.print_solution()
             print("\n\n")
         case '2':
             eight.print_solution()
             print("\n\n")
         case '3':
             nine.print_solution()
             print("\n\n")
         case '0':
             print('Bye-bye :(')
             break
         case _:
             print("Вы ввели некорректное значение\nПожалуйста введите число из списка")
             print("\n\n")
