This program takes a file input from the user that contains numbers. The program summates the numbers and returns the value as an integer. 

The program starts by reading the file lines: The first line, which represents the quanitity of numbers in the file, is seperataly read first. This is to stop the summation program from considering the first line as a part of the sum. The rest of the lines are then read in together. 

Next, the summation function converts the lines into integers and goes through all of the values in the lines. It first checks if the value is "-999" and if it is, it stops counting and exits the code. It will return whatever value the sum currently holds. Next, the function checks that the values are positive and if they are, the value is added to the sum. Once all of the lines are read, the function returns the value of the sum or "EMPTY" if the sum is 0, and the sum is printed. 

Time Complexity: O(n) 

The time complexity if O(n) because the loop increments by a constant amount, going through each case for each line. 