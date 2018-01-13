import os
import csv
import re

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

emp_csv=os.path.join('employee_data2.csv')

employee_id=[]
first_name=[]
last_name=[]
dob=[]
ssn=[]
states = []

with open(emp_csv,'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        first,last = row['Name'].split(" ")
        
        employee_id.append(row['Emp ID'])
        first_name.append(first)
        last_name.append(last)
        dob.append(row['DOB'])
        text = row['SSN']
        text = re.sub(r'\d', r'#', text, count=5)
        ssn.append(text)

        states.append(us_state_abbrev[row['State']])

clean_csv = zip(employee_id, first_name, last_name, dob, ssn, states)

with open('employee_data1.csv', 'w', newline='') as new_csv:

    writer=csv.writer(new_csv)
    
    writer.writerow(['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', "State"])
    writer.writerows(clean_csv)







