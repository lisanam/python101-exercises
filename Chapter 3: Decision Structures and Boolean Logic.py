# Chapter 3: Decision Structures and Boolean Logic

# 1. Day of the Week
# Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user enters a number that is outside the range of 1 through 7.


# 2. Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.


# 3. Age Classifier
# Write a program that asks the user to enter a person’s age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. Following are the guidelines:
# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.


# 4. Roman Numerals
# Write a program that prompts the user to enter a number within the range of 1 through 10. The program should display the Roman numeral version of that number. If the number is outside the range of 1 through 10, the program should display an error message. The following table shows the Roman numerals for the numbers 1 through 10:

'''  
  Number  1  2  3  4  5  6  7   8   9  10
  Roman   I II III IV V VI VII VIII IX  X
  Numeral
'''

# 5. Mass and Weight
# Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the amount of mass of an object in kilograms, you can calculate its weight in newtons with the following formula:
# weight = mass * 9.8
# Write a program that asks the user to enter an object’s mass, then calculates its weight. If the object weighs more than 500 newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons, display a message indicating that it is too light.


# 6. Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year: 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.


# 7. Color Mixer
# The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:
# When you mix red and blue, you get purple. When you mix red and yellow, you get orange. When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program should display the name of the secondary color that results.


# 8. Hot Dog Cookout Calculator
# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given. The program should display the following details:
# The minimum number of packages of hot dogs required
# The minimum number of packages of hot dog buns required
# The number of hot dogs that will be left over
# The number of hot dog buns that will be left over


# 9. Roulette Wheel Colors
# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
# Pocket 0 is green.
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black. The program should display an error message if the user enters a number that is outside the range of 0 through 36.


# 10. Money Counting Game
# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar.


# 11. Book Club Points
# Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
# If a customer purchases 0 books, he or she earns 0 points.
# If a customer purchases 2 books, he or she earns 5 points.
# If a customer purchases 4 books, he or she earns 15 points.
# If a customer purchases 6 books, he or she earns 30 points.
# If a customer purchases 8 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.


# 12. Software Sales
# A software company sells a package that retails for $99. Quantity discounts are given according to the following table:
'''
  Quantity 10–19 20–49 50–99 100+
  Discount  10%   20%   30%   40%
'''
  
# Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.


# 13. Shipping Charges
# The Fast Freight Shipping Company charges the following rates:
'''
  Weight of Package                                Rate per Pound
  2 pounds or less                                 $1.50
  Over 2 pounds but not more than 6 pounds         $3.00
  Over 6 pounds but not more than 10 pounds        $4.00 
  Over 10 pounds                                   $4.75
'''
# Write a program that asks the user to enter the weight of a package then displays the shipping charges.


# 14. Body Mass Index
# Write a program that calculates and displays a person’s body mass index (BMI). The BMI is often used to determine whether a person is overweight or underweight for his or her height. A person’s BMI is calculated with the following formula: 
# BMI = weight * (703 / height) ** 2
# where weight is measured in pounds and height is measured in inches. The program should ask the user to enter his or her weight and height, then display the user’s BMI. The program should also display a message indicating whether the person has optimal weight, is underweight, or is overweight. A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be underweight. If the BMI value is greater than 25, the person is considered to be overweight.


# 15. Time Calculator
# Write a program that asks the user to enter a number of seconds and works as follows:
# There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should convert the number of seconds to minutes and seconds.
# There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds.
# There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.


# 16. February Days
# The month of February normally has 28 days. But if it is a leap year, February has 29 days. Write a program that asks the user to enter a year. The program should then display the number of days in February that year. Use the following criteria to identify leap years:
# 1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
# 2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.

# Here is a sample run of the program:
'''
  Enter a year: 2008 Enter
  In 2008 February has 29 days.
'''


# 17. Wi-Fi Diagnostic Tree
# Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use the flowchart to create a program that leads a person through the steps of fixing a bad Wi-Fi connection. Here is an example of the program’s output:

'''
  Reboot the computer and try to connect. 
  Did that fix the problem? no [Enter]
  Reboot the router and try to connect. 
  Did that fix the problem? yes [Enter]
'''

# Notice the program ends as soon as a solution is found to the problem. Here is another example of the program’s output:
'''
  Reboot the computer and try to connect. 
  Did that fix the problem? no [Enter]
  Reboot the router and try to connect. 
  Did that fix the problem? no [Enter]
  Make sure the cables between the router and modem are plugged in firmly. 
  Did that fix the problem? no [Enter]
  Move the router to a new location.
  Did that fix the problem? no [Enter]
  Get a new router.
'''


# 18. Restaurant Selector
# You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:
''' 
  Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
  Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
  The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
'''

# Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, to which then displays only the restaurants to which you may take the group. Here is an example of the program’s output:
'''
  Is anyone in your party a vegetarian? yes [Enter] 
  Is anyone in your party a vegan? no [Enter]
  Is anyone in your party gluten-free? yes [Enter] 
  Here are your restaurant choices:
    Main Street Pizza Company Corner Cafe
    The Chef's Kitchen
'''

# Here is another example of the program’s output:
'''
  Is anyone in your party a vegetarian? yes [Enter] 
  Is anyone in your party a vegan? yes [Enter]
  Is anyone in your party gluten-free? yes [Enter] 
  Here are your restaurant choices:
    Corner Cafe
    The Chef's Kitchen
'''


# 19. Turtle Graphics: Hit the Target Modification
# Enhance the hit_the_target.py program that you saw in Program 3-9 so that, when the projectile misses the target, it displays hints to the user indicating whether the angle and/or the force value should be increased or decreased. For example, the program should display messages such as 'Try a greater angle' and 'Use less force.'

