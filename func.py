
incomes = []
expenses = []
history = {'his':[]}
balance = 0


#increase balance and append to history
def increase(price,desc):
    global balance
    indata = {"price":price,"desc":desc,"type":'incomes'}
    history['his'].append(indata)
    balance = balance + price
#decrease balance and append to history
def decrease(price,desc):
    global balance
    indata = {"price":price,"desc":desc,"type":'expenses'}
    print(indata['price'])
    history['his'].append(indata)
    balance = balance-price
#show current balance
def show_balance():
    global balance
    print(balance)
#show transaction_history
def transaction_history():
    print('No','price','description','type')
    for v,k in enumerate(history['his']):
        print(v,k['price'],k['desc'],k['type'])