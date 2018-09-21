file_for_reading = open('in.txt', 'r')
text_in_file = file_for_reading.read()
file-for_reading.close()

with open('in.txt', 'r') as file_for_reading:
    text_in_file = file_for_reading.read()
    
with open('in.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        print('I read a line and it is:', repr(line))
        
with open('in.txt', 'r') as _file_for_reading:
    for line in file_for_reading:
        words = line.split()
        print('I read a line and it is:', repr(words))
        
with open('imn.txt', 'r') as file for reading:
    for line in file_for_reading:
        words = line.split()
        