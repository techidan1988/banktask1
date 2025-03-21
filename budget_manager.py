
#global
from func import increase
from func import decrease
from func import show_balance
from func import transaction_history


Manager_menu ='''
Budget Manager
1. Add Income
2. Add Expense
3. Show Balance
4. Show Transaction History
5. Exit
'''
print(Manager_menu)
while True:
    num = int(input('Select an option: '))
    match num:
        case 1:
            price = input('add Income number')
            desc = input('description')
            increase(price=int(price),desc=desc)
        case 2:
            price = input('add Income number')
            desc = input('description')
            decrease(price=int(price), desc=desc)
        case 3:
            show_balance()
        case 4:
            transaction_history()
        case 5:
            break