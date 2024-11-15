def solution():
    try:
        file_name = input('Please write filename: ')
        with open(file_name, 'r') as file:
            content = file.read()
            print("The contents of the file {}:".format(file_name))
            print(content)
    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred while reading the file:", e)