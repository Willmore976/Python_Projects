'''-------------------------------------------------------------------------
Anthony Willmore
IS 340
Austin Phillip
11/4/2014
---------------------------------------------------------------------------'''
import sys
import math
state_interest = 18.5
Project_Loop = True


# Displays Menu to choose financial options

def displayMenu ():
    print ('1. Apply for a Credit Card.')
    print ('2. Calculate Monthly Loan Payments.')
    print ('3. Calculate Maturity Value of an IRA.')
    print ('Q. Quit.\n')

    Menu_Selection = raw_input('Please make a selection.(1,2,3, or Q)\n').upper()
    return Menu_Selection

# Displays how to apply for a credit card

def ApplyForCard():
    while True :
        Customer_Balance = int(raw_input('Please enter your account balance.\n'))
        if Customer_Balance <0 :
            print "Please try again, account balance cannot be negative.\n"
            continue
        if Customer_Balance >= 15000 :
            return 'Platinum'
        elif Customer_Balance >= 10000 :
            return 'Gold'
        elif Customer_Balance >= 5000 :
            return 'Silver'
        else :
            return 'Not Approved'

# Gets input from user and passes data to the calcMonthlyLoanPayment function

def getMonthlyLoanPayment() :
    while True: 
         N = int(raw_input('How many years until loan maturity?\n')) #Loan maturity
         if N < 0 :
             print 'Please try again, years cannot be negative'
             continue
         break
    while True:
         P = float(raw_input('How much is the principal of the loan?\n')) #Loan principal
         if P < 0 :
             print 'Please try again, principal cannot be negative.\n'
             continue
         break
    while True :
         R = float(raw_input('How much is the annual interest rate?')) #Annual interest rate
         if R < 0 :
             print 'Please try again, the annual interest rate cannot be negative\n'
             continue
         elif  R > state_interest :
             print 'Please try again, according to state law interest cannot exceed 18.5%\n'
             continue
         break

    Loan_Information = calcMonthlyLoanPayment(P, R, N)
    return Loan_Information

# Calculate the monthly payment on a loan, then passes it to main()

def calcMonthlyLoanPayment(LoanAmt, InterestRate, numYears) : 
    while True:
       InterestRate = InterestRate / 100.00
       monthlyRate = InterestRate / 12.00
       Monthly_Payment = (LoanAmt * monthlyRate) / (1 - math.pow ((1 + monthlyRate),(-12 * numYears)))
       return Monthly_Payment

# Gets input from user and passes data to function calcIRAMaturity()

def getIRAMaturity() :
    while True :

        currentAge =  int(raw_input('What is your current age?\n')) #Calculate Current Age
        if currentAge < 0 :
            print 'Please try again, age cannot be a negative number\n'
            continue
        elif currentAge > 65 :
            print 'Please try again, you cannot be more than 65 years old\n'
            continue
        N = (65 - currentAge)
        break
    while True :
        
        D = float(raw_input('How much is the annual deposit?\n'))  # Annual deposit ammount
        if D > 2000 : 
            print 'Please try again, annual deposit cannot be more $2,000.\n'
            continue
        elif D  <= 0 :
            print ' Must be greater than 0!\n'
            continue
        break
    while True:
            
        R = float(raw_input('Please enter the annual interest rate\n')) #Annual Interest Rate
        if R > state_interest:
            print ' Interest rate cannot be over 18.5%\n'
            continue
        break
    
    IRA_Maturity = calcIRAMaturity (N , D , R) #Passes data to calcIRAMaturity
    return IRA_Maturity

# Function that calculates IRA maturity

def calcIRAMaturity (YearUntilMaturity, AnnualDepositAmt, InterestRate):
    while True :

        InterestRates = InterestRate / 100
        M = (AnnualDepositAmt *((math.pow((1 + InterestRates), YearUntilMaturity) - 1) / InterestRates))
        return M

# Main function that displays results from each option
             
def main():

    while True :
        Menu_Selection = displayMenu()
        if Menu_Selection not in ['1', '2', '3', 'Q']:
            print "oops try again\n"
            continue
        if Menu_Selection == '1' :                              #Activates Option 1
            Card_Selection = ApplyForCard()
            if Card_Selection in ['Platinum', 'Gold', 'Silver'] :
                print 'You are eligible for a %s card' % (Card_Selection)
            else :
                 print 'You are not eligible for a card'
        if Menu_Selection == '2' :                              #Activates Option 2
            Monthly_Loan_Payment = getMonthlyLoanPayment()
            print 'Your monthly loan payment is $%.2f' % (Monthly_Loan_Payment)
        if Menu_Selection == '3' :                              #Activates Option 3
            IRA_Maturity = getIRAMaturity()
            print 'Your IRA maturity is $%.2f' % (IRA_Maturity)
        if Menu_Selection == 'Q' :                              #User Quits program
            print 'Goodbye!'
            sys.exit()
            
                
main()

