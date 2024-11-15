import string
def solution():
    try:
        input_file = input('Please write the name of the input file: ')
        output_file = input('Please write the name of the output file: ')
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
                for line in infile:
                    clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                    outfile.write(clean_line)

        print("The text has been successfully converted and written to a file '{}'.".format(output_file))
    
    except Exception as e:
        print("An error occurred while reading the file:", e)