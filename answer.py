import fileinput
import sys

def summation(lines: str) -> int:
    length: str
    sum = 0
    index = 1
   
    for line in lines:
        # translate to int values
        value = int(line)
        
        if(value == -999):
            break
        
        else:
            if(value > 0):
                sum += line
                index += 1
    if(sum == 0):
        return 'EMPTY'
    

    return sum


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    print(filename)

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
    print(summation(lines))