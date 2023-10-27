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
def debt_repayment(debt, interest_rate, annual_payment):
    monthly_interest_rate = interest_rate / 100 / 12

    monthly_payment = annual_payment / 1

    months = 0

    total_interest = 0

    while debt > 0 and monthly_payment < debt * monthly_interest_rate:
        interest = debt * monthly_interest_rate

        total_interest += interest

        debt = debt - monthly_payment + interest

        months += 1
    return months, total_interest

debt = float(input("Enter the initial debt: "))
interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
annual_payment = float(input("Enter the annual payment: "))

months, total_interest = debt_repayment(debt, interest_rate, annual_payment)

print(f"It will take {months} months to pay off the debt.")
print(f"The total amount of interest paid is ${total_interest:.2f}.")

