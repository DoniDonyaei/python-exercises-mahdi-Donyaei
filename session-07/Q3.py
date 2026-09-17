#tabe baraye list tarakonesh ha 
def analyze_transactions(transactions):
    result = {}

    #loop baraye barresi tarakonesh ha 
    for username, transaction_type, amount in transactions:
        if username not in result:
            result[username] = {
                'deposits': 0,
                'withdrawals': 0,
                'balance_change': 0,
                'transactions': 0
            }

#barresi noe tarakonesh
        if transaction_type == 'deposit':
            result[username]['deposits'] += amount

        elif transaction_type == 'withdraw':
            result[username]['withdrawals'] += amount

        result[username]['transactions'] += 1

    for username in result:
        deposits = result[username]['deposits']
        withdrawals = result[username]['withdrawals']

        result[username]['balance_change'] = deposits - withdrawals

#bishtarin deposit
    most_deposit_user = max(result, key=lambda user: result[user]['deposits'])
    
#bishtarin bardasht
    most_withdraw_user = max(result, key=lambda user: result[user]['withdrawals'])
    
#bishtarin tedad tarakonesh
    most_active_user = max(result, key=lambda user: result[user]['transactions'])

    return {
        'users': result,
        'most_deposit_user': most_deposit_user,
        'most_withdraw_user': most_withdraw_user,
        'most_active_user': most_active_user
    }

#list dade shodeye mesal
transactions = [
    ('Ali', 'deposit', 5000000),
    ('Ali', 'withdraw', 1000000),
    ('Sara', 'deposit', 8000000),
    ('Ali', 'withdraw', 500000),
    ('Sara', 'withdraw', 2000000),
    ('Reza', 'deposit', 10000000)
]

answer = analyze_transactions(transactions)

#pasokh nahaei va zire ham neveshte shodan list
for user, info in answer['users'].items():
    print('User:', user)
    print('Deposits:', info['deposits'])
    print('Withdrawals:', info['withdrawals'])
    print('Balance change:', info['balance_change'])
    print('Transactions:', info['transactions'])
    print('--------------------')

print('Most deposit user:', answer['most_deposit_user'])
print('Most withdraw user:', answer['most_withdraw_user'])
print('Most active user:', answer['most_active_user'])