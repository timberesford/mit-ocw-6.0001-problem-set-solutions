# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:04:26 2020

@author: timjo
"""
##############################################################################
## Solutions to part b of Problem Set 1 from MIT OCW 6.0001
##############################################################################

##############################################################################
## Note, part a asks for the monthly equivalent rate to be derived 
## from the annual equivalent rate, r, using r/12. I believe this to be a 
## mistake and that monthly equivalent rate should be calculated using 
## ((1+r)**1/12)-1. As such, the latter calculation is used in this code.
## The former is included but commented out so that it may be used to test
## code against test cases provided.
##############################################################################


## ASSIGNMENT OF CONSTANTS USED

# Portion of total cost required as deposit - expressed as decimal
portion_down_payment = 0.25                                       
# Savings already amassed (in £)              
current_savings = 0                                                             
# Annual equivalent rate on savings expressed as decimal
r = 0.04                                                
# Caluculates monthly equivalent rate on savings                        
monthly_r = ((1+r)**(1/12))-1

## Assign 6 to initial raise month
raise_month = 6                                                 

##############################################################################
monthly_r = r/12                                                              # Monthly r as defined by problem set- used to test code against test cases provided
##############################################################################


## RETRIEVAL OF DATA INPUTTED BY USER

# Annual, take home salary retrieved from user (problem set states assumption that this will be valid number)
annual_salary = input("Please enter your annual salary (after tax) in £: ")     
# Converts inputted value for annual_salary to float class
annual_salary = float(annual_salary)                                            

# Collects portion of income to be put aside each month as % of salary - not the way the problem set asks for the input but I prefer it
portion_saved = input("Please enter the percentage of your income you wish to put aside each month (as a % with a value between 1-100): ") 
# Converts portion_saved to float and performs float division to convert to decimal
portion_saved = float(portion_saved)/100
print(portion_saved)
120

# Retrieves cost of dream home from user                                        
total_cost = input("Please enter the cost of your dream home in £: ")
# Converts total cost to type float          
total_cost = float(total_cost)                                                 

# Collects % raise of salary - not the way the problem set asks for the input but I prefer it
semi_annual_raise = input("Please enter your semi-annual raise (as a % with a value between 1-100): ") 
# Converts portion_saved to float and performs float division to convert to decimal
semi_annual_raise = float(semi_annual_raise)/100
print(semi_annual_raise)


## CALCULATING VALUES REQUIRED TO DETERMINE RESULT

# Calculates down payment required in £
down_payment_required = portion_down_payment*total_cost                         



## CALCULATING HOW MANY MONTHS NEEDED TO REACH TARGET

# Assign zero to number of months
number_of_months = 0

# while loop to calulate savings after each month has passed, exiting once target exceeded
while current_savings < down_payment_required:
    # increase month count by 1
    number_of_months += 1      
    # multiply current savings by monthly equivalent rate to find value reached by month's end
    current_savings = current_savings*(1+monthly_r)
    # Calculates amount put away by user this month
    monthly_savings = (annual_salary/12)*portion_saved
    # increase current savings by amount put away in 1 month
    current_savings += monthly_savings
    # check if salary due to raise and execute raise if so
    if number_of_months == raise_month:
        print(annual_salary)
        # multiply salary by raise %
        annual_salary += annual_salary*semi_annual_raise
        print(annual_salary)
        # increase raise month value
        raise_month += 6
print("Number of months required to meet goal: ",number_of_months)