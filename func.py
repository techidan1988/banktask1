
incomes = []
expenses = []
history = {'his':[]}
balance = 0

### Interactive functions ###
def get_valid_float(prompt):
    while True:
        try:
            if prompt and not prompt.strip()[-1] == ":":
                prompt=prompt.strip()+": "
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a value greater than 0.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.\n")

def get_valid_string(prompt):
    if prompt and not prompt.strip()[-1] == ":":
        prompt = prompt.strip() + ": "

    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Invalid input, the string cannot be empty.\n")

def get_valid_y_n(prompt):
    if prompt:
        prompt=prompt.strip()+" (Y/n): "
    value = get_valid_string(prompt)

    while True:
        if value.lower() not in ['n','y']:
            value = get_valid_string("Y/n? ")
        else:
            break

    return value.lower() == 'y'

#increase balance and append to history
def increase():
    global balance
    while True:
        price = get_valid_float('add income number')
        desc = get_valid_string('description')
        indata = {"price":price,"desc":desc,"type":'incomes'}
        history['his'].append(indata)
        balance = balance + price

        if not get_valid_y_n("Do you want to add another income?"):
            return


#decrease balance and append to history
def decrease():
    while True:
        global balance
        price = get_valid_float('add expense number')
        desc = get_valid_string('description')
        indata = {"price":price,"desc":desc,"type":'expenses'}

        history['his'].append(indata)
        balance = balance-price

        if not get_valid_y_n("Do you want to add another expense?"):
            return

#show current balance
def show_balance():
    global balance
    print(balance)

#show transaction_history
def transaction_history():
    print('No','price','description','type')
    for v,k in enumerate(history['his']):
        print(v,k['price'],k['desc'],k['type'])