# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)

# code starts here

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here

banks = bank.drop(['Loan_ID'], axis = 1)

#print(banks.isnull().sum())

bank_mode = banks.mode()

cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

#banks[cols] = banks[cols].fillna(banks.mode().iloc[0])  -- another method

banks[cols] = banks[cols].fillna(bank_mode.iloc[0])

print(banks.isnull().sum())

#print (banks.columns)

#code ends here


# --------------
# Code starts here

#print(banks.head())

avg_loan_amount = banks.groupby(['Gender', 'Married', 'Self_Employed'])[['LoanAmount']].mean()

print(avg_loan_amount)


# code ends here



# --------------
# code starts here

loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])

print(loan_approved_se)

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])

print(loan_approved_nse)

Loan_Status = 614

percentage_se = loan_approved_se * 100 / Loan_Status

percentage_nse = loan_approved_nse * 100 / Loan_Status

print(percentage_se)
print(percentage_nse)

# code ends here


# --------------
# code starts here


loan_term = banks['Loan_Amount_Term']/12

#big_loan_term = 
big_loan_term = len(loan_term[loan_term >= 25])

print(big_loan_term)


# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


