
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
while True:
    print(Manager_menu)
    num = int(input('Select an option: '))
    match num:
        case 1:
            increase()
        case 2:
            decrease()
        case 3:
            show_balance()
        case 4:
            transaction_history()
        case 5:
            break