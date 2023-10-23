"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""
userInput = input("Will you enter the amount of time in years, months or days? ")
P = float(input("Enter the initial investment: "))
R = float(input("Enter the annual interest rate in percent form: ")) / 100
T = float(input("Enter the length of time: "))

if userInput == 'years':
  T
  I = P * R * T
  print(f"The amount of simple interest is {I:.2f}")
elif userInput == 'months':
  T / 12
  I = P * R * T 
  print(f"The amount of simple interest is {I:.2f}")
elif userInput == 'days':
  T / 365
  I = P * R * T
  print(f"The amount of simple interest is {I:.2f}")

#I = P * R * T

#print(f"The amount of simple interest is {I:.2f}")
