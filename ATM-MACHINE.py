balance = 500
while True:
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    choice = input('Choose an option: ')
    if choice == '1':
        print('Balance:',balance)
    elif choice == '2':
        amount = int(input('How much do you want to deposit: '))
        balance = amount + balance
        print('Balance:',balance)
        print('Deposit Successful!')
    elif choice =='3':
        withdraw = int(input('How much do you want to withdraw: '))
        if withdraw > balance:
            print('Insufficient funds')
        elif withdraw <= 0:
            print('Invalid amount')
        else:
            balance = balance - withdraw
            print('Balance:',balance)
            print('Withdrawal Successful!')
    elif choice == '4':
        print('Thank you for banking with TMI Bank')
        break
    else:
        print('Invalid option')