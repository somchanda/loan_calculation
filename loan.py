from tkinter import *
from tabulate import tabulate


def calculate():
    loan = float(loan_text.get())
    rate = float(rate_text.get())
    duration = int(duration_text.get())
    # To calculate interest
    interest = loan * rate / 100
    repayment = loan / duration
    repayment = round(repayment, 2)

    data = list()

    for i in range(1, int(duration + 1)):
        if i == 1:
            data.append(
                {'Period': i, 'loan': loan, 'interest': round(interest, 2),
                 'repayment': repayment, 'totalRepayment': round(interest + repayment, 2), 'balance': loan - repayment})
        else:
            data.append({'Period': i, 'loan': round(data[i - 2]['loan'] - data[i - 2]['repayment'], 2), 'interest': 0,
                         'repayment': repayment, 'totalRepayment': 0})
            data[i - 1]['interest'] = round(data[i - 1]['loan'] * rate / 100, 2)
            data[i - 1]['totalRepayment'] = round(data[i - 1]['interest'] + repayment, 2)
            data[i - 1]['balance'] = round(data[i - 1]['loan'] - data[i - 1]['repayment'], 2)
            if data[i - 1]['balance'] < 0 or data[i - 1]['balance'] < 1:
                data[i - 1]['balance'] = 0
    print(tabulate(data, headers='keys', tablefmt='grid'))


# create windows object
app = Tk()

# Loan
loan_text = StringVar()
loan_label = Label(app, text="Loan principle: ", font=('Times New Roman', 14), pady=10, padx=100)
loan_label.grid(row=0, column=0, sticky=W)
loan_entry = Entry(app, textvariable=loan_text, width=30, font=('Times New Roman', 14))
loan_entry.grid(row=0, column=1, padx=10)

# Rate
rate_text = StringVar()
rate_label = Label(app, text="Interest Rate: ", font=('Times New Roman', 14), pady=10, padx=100)
rate_label.grid(row=1, column=0, sticky=W)
rate_entry = Entry(app, textvariable=rate_text, width=30, font=('Times New Roman', 14))
rate_entry.grid(row=1, column=1, padx=10)

# Duration
duration_text = StringVar()
duration_label = Label(app, text="Duration: ", font=('Times New Roman', 14), pady=10, padx=100)
duration_label.grid(row=2, column=0, sticky=W)
duration_entry = Entry(app, textvariable=duration_text, width=30, font=('Times New Roman', 14))
duration_entry.grid(row=2, column=1, padx=10)

# Button calculate
cal_btn = Button(app, text='Calculate', width=20, command=calculate)
cal_btn.grid(row=3, column=1, padx=10, sticky=W, pady=10)

app.title("Loan calculate system")
app.geometry('1080x720')

# start program
app.mainloop()
