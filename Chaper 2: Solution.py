# Chaper 2: Input, Processing, and Output

# 1. Personal Information
# Your name
print("Lisa")
# Your address, with city, state, and ZIP
print("123 Address, City, ST, 00000")
# Your telephone number
print("123-456-7890")
# Your college major
print("Computer Science")


# 2. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

# A profit margin is 23%
profit_margin = .23
# Get total sales from user & convert the input string to a float
total_sales = float(input("What is the total sales:"))
# Give annual profit to user by multiplying total sales with profit margin
print(f'Annual profit is: ${total_sales * profit_margin: .02f}')


# 3. Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to enter the total square feet in a tract of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43,560 to get the number of acres.

# Ask user for area in feet & convert it into float
feet = float(input('Enter the area in square feet:'))
# Print the area in acre
print(f'Here is the area is: {feet / 43560} acre')


# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of each item, then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.

# Establish tax rate
tax_rate = 0.07
# Ask for price of 5 items
item1 = float(input('Enter the price of the first item:'))
item2 = float(input('Enter the price of the second item:'))
item3 = float(input('Enter the price of the third item:'))
item4 = float(input('Enter the price of the fourth item:'))
item5 = float(input('Enter the price of the fifth item:'))
# Get subtotal
subtotal = item1 + item2 + item3 + item4 + item5
# Display the subtotal, the sales tax, and the total
print(f'''Subtotal: ${subtotal: .2f}
Tax: ${subtotal * tax_rate: .2f}
Total: ${subtotal * (1 + tax_rate): .2f}''')


# 5. Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated with the following formula:
# Distance = Speed * Time
# A car is traveling at 70 miles per hour. Write a program that displays the following:
# The distance the car will travel in 6 hours
# The distance the car will travel in 10 hours
# The distance the car will travel in 15 hours

# Establish the speed of the car
speed = 70
# Print Distance travelled after 6 hours
print(f'The distance travelled after 6 hours: {speed * 6} miles')
# Print Distance travelled after 10 hours
print(f'The distance travelled after 10 hours: {speed * 10} miles')
# Print Distance travelled after 15 hours
print(f'The distance travelled after 15 hours: {speed * 15} miles')


# 6. Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state and county sales tax. Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

# Establish the state and county sales tax rate
state_tax_rate = 0.05
county_tax_rate = 0.025
# Ask for the purchase subtotal & convert it to float
subtotal = float(input('Please enter the purchase subtotal:'))
# Print the subtotal, state tax, county tax, and total
print(f'''Subtotal: ${subtotal: .2f}
State Tax: ${subtotal * state_tax_rate: .2f}
County Tax: ${subtotal * county_tax_rate: .2f}
Total: ${subtotal * (1 + state_tax_rate + county_tax_rate): .2f}''')


# 7. Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven ÷ Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car's MPG and display the result.

# Ask user for the number of miles driven & convert it to float
distance = float(input('Enter the number of miles driven:'))
# Ask user for the gallons of gas used & convert it to float
gas = float(input('Enter the gallons of gas used:'))
# Print car's MPG
print(f'MPG: {distance / gas} miles per gallon')

# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

#Set tip, Tax
tax = .07
tip = .18
#Ask user for price of the meal & convert to float
price = float(input("Enter the price of the meal:"))
#Give tax, tip, total by multiplying it with price
print(f'''Tax: {price * tax: .2f}
Tip: {price * tip: .2f}
Total: {price * (1 + tax + tip): .2f}''')


# 9. Celsius to Fahrenheit Temperature Converter
# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
# F = (9/5)C + 32
# The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.

# Ask your for the temperature in Celsius & covert it to float
c = float(input('Enter the temperature in Celsius:'))
# Display the temperature in Fahrenheit
print(f'Here is the temperature in Fahrenheit: {c * 9 / 5 + 32: .1f} F')


# 10. Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies.

# Establish the recipe per cookie
sugar_per_cookie = 1.5/48
butter_per_cookie = 1/48
flour_per_cookie = 2.75/48
# Ask user for the number of cookies he or she wants to make & covert it to int
cookie = int(input('How many cookies do you want to make?'))
# Display the amount of sugar, butter, and flour needed in cups
print(f'''For {cookie: d} cookies:
Sugar: {sugar_per_cookie * cookie: .2f} cups
Butter: {butter_per_cookie * cookie: .2f} cups
Flour: {flour_per_cookie * cookie: .2f} cups''')


# 11. Male and Female Percentages
# Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class.
# Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

# Ask the number of female students & convert it to int
female = int(input("Enter the number of female students:"))
# Ask the number of male students & convert it to int
male = int(input("Enter the number of male students:"))
# Get the total number of students
total = female + male
# Display percentage of male and female students
print(f'''The percentage of female students: {female / total * 100: .1f}%
The percentage of male students: {male / total * 100: .1f}%''')


# 12. Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
# The number of shares that Joe purchased was 2,000.
# When Joe purchased the stock, he paid $40.00 per share.
# Joe paid his stock broker a commission that amounted to 3 percent of the amount he paid for the stock.

# Two weeks later, Joe sold the stock. Here are the details of the sale:
# The number of shares that Joe sold was 2,000.
# He sold the stock for $42.75 per share.
# He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.

# Write a program that displays the following information:
# The amount of money Joe paid for the stock.
price_buy = 2000 * 40
print(f'The amount of money Joe paid for the stock: ${price_buy}')
# The amount of commission Joe paid his broker when he bought the stock.
buy_broker_fee = price_buy * 0.03
print(f'The amount of money Joe paid for the broker when he bought the stock: ${buy_broker_fee}')
# The amount for which Joe sold the stock.
price_sell = 2000 * 42.75
print(f'The amount of money Joe received for the broker: ${price_sell}')
# The amount of commission Joe paid his broker when he sold the stock.
sell_broker_fee = price_sell * 0.03
print(f'The amount of money Joe paid for the broker when he sold the stock: ${sell_broker_fee}')
# Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.
print(f'The total money Joe made is ${price_sell - price_buy - buy_broker_fee - sell_broker_fee}')

# 13. Planting Grapevines
# A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row. She has determined that after measuring the length of a future row, she can use the following formula to calculate the number of vines that will fit in the row, along with the trellis end-post assemblies that will need to be constructed at each end of the row:  V = (R - 2E)/S

# The terms in the formula are:
# V is the number of grapevines that will fit in the row.
# R is the length of the row, in feet.
# E is the amount of space, in feet, used by an end-post assembly. 
# S is the space between vines, in feet.

# Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
# The length of the row, in feet
R = int(input('Enter the length of the row, in feet'))
# The amount of space used by an end-post assembly, in feet
E = int(input('Enter the amount of space used by an end-post assembly, in feet'))
# The amount of space between the vines, in feet
S = int(input('Enter the amount of space between the vines, in feet'))
# Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.
print(f'The number of grapevines that will fit in the row: {(R - (2 * E)) / S} grapevines')


# 14. Compound Interest
# When a bank account pays compound interest, it pays interest not only on the principal amount that was deposited into the account, but also on the interest that has accumulated over time. Suppose you want to deposit some money into a savings account, and let the account earn compound interest for a certain number of years. The formula for calculating the balance of the account after a specified number of years is: A = P(1 + (r/n)) ** nt

# The terms in the formula are:
# A is the amount of money in the account after the specified number of years. P is the principal amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year that the interest is compounded.
# t is the specified number of years.

# Write a program that makes the calculation for you. The program should ask the user to input the following:
# The amount of principal originally deposited into the account
P = float(input("Enter the principal:"))
# The annual interest rate paid by the account
r = float(input("Enter the annual interest rate as a percentage:")) / 100
# The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)
n = float(input("Enter the number of times per year that the interest is compounded:"))
# The number of years the account will be left to earn interest 
t = float(input("Enter the number of years the account will be left to earn interest:"))
# Once the input data has been entered, the program should calculate and display the amount of money that will be in the account after the specified number of years.
print(f'The total money in the account is ${P * (1 + (r/n)) ** (n * t)}')
# NOTE: The user should enter the interest rate as a percentage. For example, 2 percent would be entered as 2, not as .02. The program will then have to divide the input by 100 to move the decimal point to the correct position.

#15. Turtle Graphics Drawings
# Use the turtle graphics library to write programs that reproduce each of the designs shown in Figure 2-40.

