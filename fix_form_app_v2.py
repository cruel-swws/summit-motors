import re
import csv
from io import StringIO

def get_mapping():
    m = {
        'firstName': 'First Name',
        'middleName': 'Middle Name',
        'lastName': 'Last Name',
        'email': 'Email Address',
        'phone': 'Home/Cell Phone',
        'address': 'Street Address',
        'unit': 'Unit Number',
        'city': 'City',
        'state': 'State',
        'zip': 'Zip Code',
        'dlState': 'DL State',
        'dlNumber': 'Drivers License Number',
        'dlIssue': 'DL Issue Date',
        'dlExp': 'DL Expiration',
        'ssn': 'Social Security Number',
        'dob': 'Date of Birth',
        'downPayment': 'Down Payment',
        'creditDesc': 'Credit Condition',
        'vehicle': 'Vehicle of Interest',
        'openLoans': 'Open Auto Loans',
        'loanBank': 'Loan Bank Name',
        'repos': 'Recent Repossessions',
        'bankName': 'Primary Bank Name',
        'savingsAccount': 'Has Savings Account',
        'checkingAccount': 'Has Checking Account',
        'prepaidCard': 'Has Prepaid Card',
        'tradeIn': 'Trade-in Details',
        'housing': 'Housing Status',
        'rentAmount': 'Monthly Rent/Mortgage',
        'yearsAtAddress': 'Years at Address',
        
        'prevAddress1': 'Prev Address 1',
        'prevUnit1': 'Prev Unit 1',
        'prevDates1': 'Prev Dates Lived 1',
        'prevCity1': 'Prev City 1',
        'prevState1': 'Prev State 1',
        'prevZip1': 'Prev Zip 1',
        
        'empType': 'Employment Type',
        'empName': 'Employer Name',
        'empTitle': 'Employer Title/Position',
        'empPhone': 'Employer Phone',
        'empAddress': 'Employer Address',
        'empCity': 'Employer City',
        'empState': 'Employer State',
        'empZip': 'Employer Zip',
        'empSalary': 'Gross Monthly Salary',
        'empYears': 'Years Employed',
        'empDate': 'Hire Date',
        
        'ref1Name': 'Reference 1 Name',
        'ref1Phone': 'Reference 1 Phone',
        'ref1Rel': 'Reference 1 Relation',
        
        'source': 'How did you hear about us',
        'referralDetails': 'Referral Details',
        'terms': 'Accepted Terms',
    }
    return m

def main():
    m = get_mapping()
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # ensure all keys in mapping exist in html names
    old_names = []
    for match in re.finditer(r'<(input|select|textarea)[^>]+name=["\']([^"\']+)["\']', html):
        old_names.append(match.group(2))
    
    new_names = [m.get(name, name) for name in old_names]
    
    def replace_name(match):
        full = match.group(0)
        tag = match.group(1)
        name = match.group(2)
        new_name = m.get(name, name)
        # carefully replace name="X" with name="Y"
        repl = re.sub(r'name=["\']' + re.escape(name) + r'["\']', f'name="{new_name}"', full)
        return repl
        
    new_html = re.sub(r'<(input|select|textarea)[^>]+name=["\']([^"\']+)["\']', replace_name, html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Updated index.html")
    
    # Update CSV!
    # Rows:
    # Row 1 is headers.
    # Row 2 is Renato's sample.
    # Row 3 is Juliana's sample.
    
    # Old keys we want to map into the new 82 column positions
    r2_data = {
        'Vehicle of Interest': '2018 Tesla Model 3',
        'First Name': 'RENATO',
        'Last Name': 'MIRANDA DE CARVALHO MELO',
        'Email Address': 'renatomiranda1@icloud.com',
        'Home/Cell Phone': '6508229210',
        'Date of Birth': '1990-06-20',
        'Social Security Number': '***-**-2649',
        'Street Address': '7304 Malakai Circle',
        'City': 'Roseville',
        'State': 'CA',
        'Zip Code': '95747',
        'Housing Status': 'Rent',
        'Monthly Rent/Mortgage': '1300',
        'Employer Name': 'dd',
        'Employer Title/Position': 'driver',
        'Gross Monthly Salary': '"$57,156"',
        'Accepted Terms': 'on'
    }
    
    r3_data = {
        'Vehicle of Interest': '2016 Kia Sedona LX',
        'First Name': 'JULIANA',
        'Last Name': 'ORELLANA',
        'Home/Cell Phone': '8313838551',
        'Date of Birth': '1996-05-01',
        'Social Security Number': '619900257',
        'Street Address': '1872 JUDSON ST',
        'City': 'SEASIDE',
        'State': 'CA',
        'Zip Code': '93955',
        'Housing Status': 'Own',
        'Monthly Rent/Mortgage': '0',
        'Employer Name': 'OG Cleaning Services ',
        'Employer Title/Position': 'Scheduler/cleaner',
        'Gross Monthly Salary': '48000',
        'Accepted Terms': 'on'
    }
    
    with open('Financing Applications - Página1.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_names)
        
        row2 = []
        for n in new_names:
            v = r2_data.get(n, '')
            if v and v.startswith('"') and v.endswith('"'):
                v = v[1:-1] # csv writer handles quoutes
            row2.append(v)
        writer.writerow(row2)
            
        row3 = []
        for n in new_names:
            v = r3_data.get(n, '')
            if v and v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            row3.append(v)
        writer.writerow(row3)
        
    print("Updated Financing Applications - Página1.csv")

if __name__ == "__main__":
    main()
