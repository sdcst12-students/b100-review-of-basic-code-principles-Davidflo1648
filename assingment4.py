"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""
def monthly_payment (principal, annual_rate, annual_payment):
  monthly_rate = annual_rate / 12
  monthly_payment = annual_payment / 12
  balance = principal
  months = 0
  while balance > 0:
    balance = balance * (1 + monthly_rate)
    balance = balance - monthly_payment
    months = months + 1
  return months, balance

def total_interest (principal, annual_rate, months):
  monthly_rate = annual_rate / 12
  interest = 0
  balance = principal
  for i in range (months):
    interest = interest + balance * monthly_rate
    balance = balance - monthly_payment (principal, annual_rate, annual_payment) [0]
    if balance < 0:
      balance = 0
  return interest

principal = float (input ("Enter the initial debt: "))
annual_rate = float (input ("Enter the annual interest rate: "))
annual_payment = float (input ("Enter the annual payment: "))

months, balance = monthly_payment (principal, annual_rate, annual_payment)
print ("It will take", months, "months to repay the debt.")
print ("The remaining balance after", months, "months is", round (balance, 2))

interest = total_interest (principal, annual_rate, months)
print ("The total amount of interest paid is", round (interest, 2))

