def read_file(filename=""):
    """a Fuction to open a file and print out the output"""
    with open(filename,'r',ecncoding = 'utf-8') as file:
        for line in file:
            print(line, end='')
