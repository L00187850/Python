#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Calculating income tax. Added on the 30% tax bracket on top of 20% and 40%.

income = 82548
single_person_tax_allowance = 42000
taxable_At_20_Percent = income - single_person_tax_allowance
taxable_At_30_Percent = income - taxable_At_20_Percent
taxable_At_40_Percent = income - taxable_At_30_Percent
percent_tax_20 = taxable_At_20_Percent * .2
percent_tax_30 = taxable_At_30_Percent * .3
percent_tax_40 = taxable_At_40_Percent * .4
total_tax = percent_tax_20 + percent_tax_30 + percent_tax_40

print(total_tax)