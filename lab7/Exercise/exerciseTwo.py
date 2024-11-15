def solution():
    try:
        file_name = input('Please write filename: ')
        n = int(input('Please write number N: '))
        with open(file_name, 'w') as file:
            for i in range(1, n+1):
                file.write(str(i) + '\n')

        print("The numbers have been successfully written to the file '{}'.".format(file_name))

        with open(file_name, 'r') as file:
            print("The contents of the file '{}':".format(file_name))
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", e)