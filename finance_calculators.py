#This is a python program that allows users to access two different financial calcualtors: an investment calculator and a home loan repayment calculator
#Function to calcualte simple and compound interest
#The user inputs initial amount, interest rate and number of years of investment
#The program outputs the total amount earnt on their investments

#Function to calculate simple interest
def calculate_simple_interest():
    initial_amount = float(input("What is the amount of money that you are depositing?"))
    interest_rate = float(input("What is the interest rate as a percentage?"))
    years = int(input("How many years are you planning on investing?"))
#Calculate simple interest using the formula A=P(1+rxt)
    r = interest_rate / 100
    x = 1 + r * years
    simple_interest = initial_amount * x
 #Calculate the total amounts and format it to 2 decimal places
    total_amount = initial_amount + simple_interest
    formatted_total_amount = format(total_amount, '.2f')
 #print the total amount earned after the specified years
    print(f"The total amount after {years} years is: {formatted_total_amount}")

#Function to calculate compound interest
def calculate_compound_interest():
#Calculate compound interest using the formula A=P(1+r)^t
    initial_amount = float(input("What is the amount of money that you are depositing?"))
    interest_rate = float(input("What is the interest rate as a percentage?"))
    years = int(input("How many years are you planning on investing?"))
    r = interest_rate / 100
    import math
    compound_interest = initial_amount * math.pow((1+r), years)
#Calculate the total amounts and format it to 2 decimal places
    total_amount = initial_amount + compound_interest
    formatted_total_amount = format(total_amount, '.2f')
#print the total amount earned after the specified years
    print(f"The total amount after {years} years is: {formatted_total_amount}")

#Function to calcualte bond repayment
#The user inputs the current value of the house, the annual interest rate, and the number of months they plan on taking to repay the bond
#The program then outputs the total amount they will pay back each month for the specified months

def calculate_bond():
   house_value = int(input("What is the present value of the house?"))
   annual_interest_rate = int(input("What is the annual interest rate as a percentage?"))
   months = int(input("What is the number of months you plan to take to repay the bond?"))
#Calcuate monthly repayment using the formula (i x P)/(1)-(1+i)^-n
   x = annual_interest_rate/100
   i = x / 12
#Calculate the repayment and format it to 2 decimal places
   repayment = (i*house_value) / (1 - (1 + i)**(-months))
   formatted_repayment = format(repayment, '.2f')
#print the total amount to repay each month for the specified years
   print(f"The total amount to repay each month for {months} months is: {formatted_repayment}")

#Display the options for the user
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#Ask the user to input their choice
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()

#peform actions based on the users choice
if user_choice == 'investment':
#If user picks investments ask user what type of interest would they like
    type = input("Do you want a simple or compound interest?").lower() 
    if type == 'simple':
        calculate_simple_interest()

    elif type == 'compound':
        calculate_compound_interest()

if user_choice == 'bond':
   calculate_bond()