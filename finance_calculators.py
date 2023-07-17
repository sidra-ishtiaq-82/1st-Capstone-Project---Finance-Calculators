import math

print ("----------Finance Calculator------------")        # Using this for the purpose of making the executed result look neat, presentable and easy to read.
print ("Investment - To calculate the amount of interest you'll earn on your investment.")
print ("Bond - To calculate the amount you'll have to pay on a home loan.\n")

menu_selection = input ("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
menu_selection = menu_selection.lower()  # The user can enter their selection in all lower, all upper or captalised case and this will just make sure
                        # the selection is accepted and stored in a uniform lower case which will then help in smooth execution of if statments.  

# Initially I had used the if statment with 'and' to define every possibility of mixed cases the user could enter their selection in,
# but that resulted in a really long if statement and after discussing it with a fellow bootcamper Peter, I agreed to his suggestion of using the
# .lower() method to keep the code short and simple.

# Following if statment will execute if user enters any string or integar other than the given choices in menu_selection and
# warn the user to select from the choices provided.
if menu_selection != "investment" and menu_selection != "bond" :
        print ("\nError: Please select one of the above choices only.")

print ("----------------------")

# Nested if statments to excute if the user enters 'investment'. 
# Prompt user to enter details in the form of integers and apply the relevant investment formula also based
# on their selection of simple or compound interest.
if menu_selection == "investment" :
    deposit_amt = int (input ("Please enter the amount of money being deposited: ")) 
    interest_rate = int (input ("Please enter your preffered percentage of interest rate: "))/100       # Interest entered, divided by 100.
    duration_inv = int (input ("Please enter the number of years you would like to invest for: "))
    interest = input ("Please choose if you want 'Simple' or 'Compound' Interest: ")
    interest = interest.lower()        # Again using this to store the value in lower case, irrespective of lower, upper or capitalised case user enters.
    

    if interest == "simple" :
        simple_interest = deposit_amt * (1 + interest_rate * duration_inv)      # Simple interest formula
        print ("------------------------")
        print (f"This is the amount of simple interest you'll earn on your Investment: {simple_interest}" )
        print ("------------------------")

    elif interest == "compound" :
        compound_interest = deposit_amt * math.pow ((1 + interest_rate), duration_inv)      # Compound interest formula
        print ("------------------------")
        print (f"This is the amount of compound interest you'll earn on your Investment: {compound_interest}" )
        print ("------------------------")


# Else if statment to execute if user selects 'bond' instead of 'investment'. 
# Prompt user to input the required details, apply the bond formula and print the result for user.
elif menu_selection == "bond" :
    house_value = int (input ("Please enter the present value of the house: "))
    interest_rate1 = int (input("Please enter the percentage of interest rate: "))/100  # For user to enter annual interest rate, divided by 100.
    duration_bond = int (input("Please enter the number of months you will take to repay the Bond: "))
    montly_interest = interest_rate1 / 12   # To convert annual interest rate into monthly interest by dividing by 12. 
    
    repayment = (montly_interest * house_value) / (1 - (1 + montly_interest) ** (- duration_bond) ) 
    print ("----------------------------")
    print (f"The amount to repay the home loan for each month is: {repayment}")
    print ("----------------------------")