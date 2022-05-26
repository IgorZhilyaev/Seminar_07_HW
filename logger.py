from datetime import datetime
import output

def log_to_file(entry):
    b = output.style()
    if b == 1:
        with open('phone.csw', 'a') as file:
            file.write(f'{datetime.today()};{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n')
    
    if b == 2:
        with open('phone.csw', 'a') as file:
            file.write(f'{datetime.today()}\n;{entry[0]}\n;{entry[1]}\n;{entry[2]};\n{entry[3]}\n')

def reading(param):
    with open('phone.csv', 'r') as file:
        for line in file:
            if param in line:
                stroka = line
                print(line)

def read_all_file():
    with open('phone.csv', 'r') as file:
        for line in file:
            print(line)