'''
######################################################
        Laboratory work No. 6 on programming
    Completed by: Savinova Alina Konstantinovna
                Option: 22 Flow: 1.3
######################################################
'''

from exercise_three import SubByoerMoore
from exercise_two import ComparisonOrChoice
from exercise_first import GameWithDice
start = "Пожалуйста выберите команду из списка и введите соответствующий ей номер:"
help = "Список комманд:\n 1. Задание №1 (\"Игра с костями\").\n2. Задание №2 (\"Сравнение или выбор?\")." + "\n3. Задание №3 (\"Плагиат или сам?\").\n0. Выход из программы (\":(\")"

print(start)
print(help)

while True:
    match input():
        case "1":
            print("Вы выбрали: Задание №1")
            print("Бог не играет в кости, но люди могут, давай поиграем")
            print("Я покажу тебе один интересный график ^_^, условия ты уже знаешь")
            GameWithDice.write_graph()
            continue
        case "2":
            print("Вы выбрали: Задание №2")
            print("Сравнив")
            ComparisonOrChoice.print_result()
            continue
        case "3":
            print("Вы выбрали: Задание №3")
            print("Сам писал или где-то списал?... Сейчас узнаем")
            SubByoerMoore.print_answer(SubByoerMoore.plagiarism_percentage)
            #SubByoerMoore.print_answer(SubByoerMoore.plagiarism_percentage_duplicate)
            if SubByoerMoore.plagiarism_percentage > 60:
                print("Ай-ай-ай, списывать не хорошо... >_<")
            else:
                print("Молодец, хорошая работа! <3")
            continue
        case "0":
            print("Надеюсь увидеть тебя ещё! Пока-пока :(")
            break
        case default:
            print("Упс..., кажется вы ввели номер не существующей команды. Пожалуйста, повторите попытку <3")
            print("Хотите вывести список доступных комманд? (Да - 'Yes' или 1; Нет - 'No' или 0)")
            answer = input()
            if answer == "Yes" or answer == "1":
                print("Хорошо, вот список доступных комманд:")
                print(help)
            else:
                print("Отлично, введите пожалуйста команду: ")
            continue