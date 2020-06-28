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

import time

## ASSIGNMENT OF CONSTANTS USED

# Portion of total cost required as deposit - expressed as decimal
portion_down_payment = 0.25                                       
# Savings already amassed (in £)              
current_savings = 0                                                             
# Annual equivalent rate on savings expressed as decimal
r = 0.04                                                
# Calculates monthly equivalent rate on savings                        
monthly_r = ((1+r)**(1/12))-1

## Assign 6 to initial raise month
raise_month = 6                                                 

## Assign £1M as dream house cost
total_cost = 1000000

# Calculates down payment required in £
down_payment_required = portion_down_payment * total_cost  

## Assign 7% to semi annual raise
semi_annual_raise = 0.07

## Assign 36 to number of months to save in
number_of_months_max = 36

## Assign £100 to accuracy margin for final value to fall within
accuracy = 100

##############################################################################
# Monthly r as defined by problem set- used to test code against test cases provided
monthly_r = r/12                                                              
##############################################################################


## RETRIEVAL OF DATA INPUTTED BY USER

# Annual, take home salary retrieved from user and converted to float (problem set states assumption that this will be valid number)
annual_salary_initial = float(input("Please enter your annual salary (after tax) in £: "))
        


## CALCULATING VALUES REQUIRED TO DETERMINE RESULT

                    

## CALCULATING PORTION SAVED VALUE USING BISECTION SEARCH

# Assign zero to number of months - this will be used to determine when to raise etc.
number_of_months = 0
    

## Assign 50% as first guess of portion saved
portion_saved = 0.5

## Assign 10000 to decimal accuracy factor
decimal_accuracy_factor = 10000

## Assign 0 to Bisection step counter
bisection_step_count = 0

## Assign values to initialise max and min used for bisection search
max_bs = decimal_accuracy_factor
min_bs = 0

# While loop to continue running calculation until sufficient accuracy is met
while abs(current_savings - down_payment_required)>accuracy:  
       
    # increase bisection step count by 1
    bisection_step_count += 1

    ## RESET VALUES TO DEFAULT
    current_savings = 0
    annual_salary = annual_salary_initial
    number_of_months = 0
    raise_month = 6
    
    
    # loop to run calculation for number of months specified
    for x in range(number_of_months_max):
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
            # multiply salary by raise %
            annual_salary += annual_salary*semi_annual_raise
            # increase raise month value
            raise_month += 6
            
    # convert portion saved to integer between 0 - decimal accuracy factor
    portion_saved = decimal_accuracy_factor*portion_saved
    
    # check if current savings lower than target
    if current_savings - down_payment_required <0:
        # make the current value the new minimum to increase next value
        min_bs = portion_saved
    # else, current savings must be higher than target
    elif current_savings - down_payment_required >0:
        # make the current value the new maxium to reduce the next value
        max_bs = portion_saved
    ## assign new portion saved value using new min/max value and normalise to decimal again - round so that integer value used
    portion_saved = round((min_bs + max_bs)/(2))
    
    # convert to decimal again
    portion_saved = portion_saved/decimal_accuracy_factor
    
    # Break the loop if bisection search has taken more than 1000 steps
    if(bisection_step_count>1000):
        break
    
# Print error message if bisection search took more than 1000 steps
if(bisection_step_count>1000):
    print("It is not possible to pay the down payment in three years.")

# print results to user        
else: 
    print("Best Savings rate: ",portion_saved)
    print("Steps in bisection search: ", bisection_step_count)
