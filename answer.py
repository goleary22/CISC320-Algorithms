import fileinput
import sys

def summation(lines: str) -> int:
    length: str
    sum = 0
    index = 0
   
    for line in lines:
        # translate to int values
        value = int(line)
        #stops when encounter -999
        if(value == -999):
            break
        else:
            if(value > 0): #only adds to sum if positive value
                sum += value
                index += 1
    if(sum == 0): #returns empty if there are no values
        return 'EMPTY'
    

    return sum


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()
    #print(filename)

    # Open the file and read in its contents
    with open(filename) as data_file:
        number_of_lines = data_file.readline() #read first line- quantity
        lines = data_file.readlines()

    # Actually do the work
    print(summation(lines))