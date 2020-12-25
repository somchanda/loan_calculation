
from tabulate import tabulate
from datetime import datetime, timedelta
import calendar
loan = input('Enter loan ($): ')
rate = input('Enter interest rate(%): ')
duration = input('Enter duration(monthly): ')
# dateReceive = input('Enter date receive (dd-mm-YYYY): ')
# dateReceive = datetime.strptime(dateReceive, '%d-%m-%Y')
# datePayment = input('Enter date to start payment(dd-mm-YYYY): ')
# datePayment = datetime.strptime(datePayment, '%d-%m-%Y')
loan = float(loan)
rate = float(rate)
duration = int(duration)
# To calculate interest
interest = loan * rate / 100
repayment = loan / duration
repayment = round(repayment, 2)
# To increase date 1 month
# dayInMonth = calendar.monthrange(dateReceive.year, dateReceive.month)[1]

data = list()

for i in range(1, int(duration + 1)):
    if i == 1:
        data.append(
            {'Period': i, 'loan': loan, 'interest': round(interest, 2),
             'repayment': repayment, 'totalRepayment': round(interest + repayment, 2), 'balance': loan - repayment})
    else:
        # dayInMonth = calendar.monthrange(datePayment.year, datePayment.month)[1]
        # date = datetime.strptime(data[i - 2]['date'], '%d-%m-%Y')
        # date = date + timedelta(days=dayInMonth)
        # date = date.strftime('%d-%m-%Y')
        data.append({'Period': i, 'loan': round(data[i-2]['loan'] - data[i-2]['repayment'], 2), 'interest': 0,
                     'repayment': repayment, 'totalRepayment': 0})
        data[i-1]['interest'] = round(data[i-1]['loan'] * rate / 100, 2)
        data[i-1]['totalRepayment'] = round(data[i-1]['interest'] + repayment, 2)
        data[i-1]['balance'] = round(data[i-1]['loan'] - data[i-1]['repayment'], 2)

# for i in range(len(data)):
#     cDate = datetime.strptime(data[i]['date'], '%d-%m-%Y')
#     weekDay = datetime.weekday(cDate)
#     if weekDay == 5:
#         tmpDate =cDate + timedelta(days=2)
#         data[i]['date'] = tmpDate.strftime('%d-%m-%Y')
#     if weekDay == 6:
#         tmpDate = cDate + timedelta(days=1)
#         data[i]['date'] = tmpDate.strftime('%d-%m-%Y')
print(tabulate(data, headers='keys', tablefmt='grid'))