# Chapter 6: Files and Exceptions

# 1. File Display
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program that displays all of the numbers in the file.


# 2. File Head Display
# Write a program that asks the user for the name of a file. The program should display only the first five lines of the file’s contents. If the file contains less than five lines, it should display the file’s entire contents.


# 3. Line Numbers
# Write a program that asks the user for the name of a file. The program should display the contents of the file with each line preceded with a line number followed by a colon. The line numbering should start at 1.


# 4. Item Counter
# Assume a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk. Write a program that displays the number of names that are stored in the file. (Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number of items that are read from the file.)


# 5. Sum of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program that reads all of the numbers stored in the file and calculates their total.


# 6. Average of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program that calculates the average of all the numbers stored in the file.


# 7. Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.


# 8. Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. Write another program that reads the random numbers from the file, displays the numbers, then displays the following data:
# The total of the numbers
# The number of random numbers read from the file


# 9. Exception Handing
# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
# It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.


# 10. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard input, then save these as records in a file named golf.txt. (Each record will have a field for the player’s name and a field for the player’s score.)
#2. A program that reads the records from the golf.txt file and displays them. 11. Personal Web Page Generator


# Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen:
'''
Enter your name: Julie Taylor [Enter]
Describe yourself: I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app developer after I graduate. [Enter]
'''


# Once the user has entered the requested input, the program should create an HTML file, containing the input, for a simple Web page. Here is an example of the HTML content, using the sample input previously shown:
'''
  <html>
  <head>
  </head>
  <body>
    <center>
      <h1>Julie Taylor</h1>
    </center>
    <hr />
    I am a computer science major, a member of the Jazz club,
    and I hope to work as a mobile app developer after I graduate. <hr />
  </body>
  </html>
'''


# 12. Average Steps Taken
# A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories burned, heart rate, sleeping patterns, and so on. One common physical activity that most of these devices track is the number of steps you take each day.
# If you have downloaded this book’s source code from the Computer Science Portal, you will find a file named steps.txt in the Chapter 06 folder. (The Computer Science Portal can be found at www.pearsonhighered.com/gaddis.) The steps.txt file contains the number of steps a person has taken each day for a year. There are 365 lines in the file, and each line contains the number of steps taken during a day. (The first line is the number of steps taken on January 1st, the second line is the number of steps taken on January 2nd, and so forth.) Write a program that reads the file, then displays the average number of steps taken for each month. (The data is from a year that was not a leap year, so February has 28 days.)
