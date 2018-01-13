#import csv
import os
import csv
import collections

bank_csv=os.path.join('budget_data_1.csv')

date=0
revenue=1
revenue_change=[]

with open(bank_csv, newline='',) as csvfile:
    csv_read=csv.reader(csvfile)
    header=next(csv_read)
    
    total_revenue = 0
    number_of_mo = 0
    sum_revenue = 0
    rev_delta = 0
    previous_revenue = 0
    
    for row in csv_read:
        current_revenue = int(row[revenue])
        if (previous_revenue == 0):
            previous_revenue = current_revenue
        else:
            sum_revenue += current_revenue - previous_revenue
            rev_delta = current_revenue - previous_revenue
            previous_revenue = current_revenue

        number_of_mo += 1
        total_revenue += int(row[revenue])
        revenue_change.append(rev_delta)
            
avg_rev = sum_revenue / number_of_mo
great_inc_rev = max(revenue_change)

great_dec_rev = min(revenue_change)

print('Financial Analysis:')
print('-------------------')  
print('Number of Months: '+ str(number_of_mo))
print('Total Amount of Revenue: '+ str('{:0,.2f}'.format(total_revenue)))
print('Average Monthly Change in Revenue: '+str('{:0,.2f}'.format(avg_rev)))
print('Greatest Monthly Increase in Revenue: '+str('{:0,.2f}'.format(great_inc_rev)))
print('Greatest Monthly Decrease in Revenue: '+str('{:0,.2f}'.format(great_dec_rev)))

with open('out_py_bank.txt','w') as text:
    text.write('Financial Analysis:')
    text.write('\n')
    text.write('-------------------')
    text.write('\n')  
    text.write('Number of Months: '+ str(number_of_mo))
    text.write('\n')
    text.write('Total Amount of Revenue: '+ str('{:0,.2f}'.format(total_revenue)))
    text.write('\n')
    text.write('Average Monthly Change in Revenue: '+str('{:0,.2f}'.format(avg_rev)))
    text.write('\n')
    text.write('Greatest Monthly Increase in Revenue: '+str('{:0,.2f}'.format(great_inc_rev)))
    text.write('\n')
    text.write('Greatest Monthly Decrease in Revenue: '+str('{:0,.2f}'.format(great_dec_rev)))