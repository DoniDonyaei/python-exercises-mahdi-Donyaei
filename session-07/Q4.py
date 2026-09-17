#shart mashkook boodan : mablagh bishtar az 100 va bish az 3 bardasht posht sare ham va mablagh bardasht bishtar az mojoodi

#mablaghe tarakonesh ra migirim va barresi mikonim ke az 100 bishtar ast ya na agar bishtar bood mashkook ast
def check_large_transaction(amount):
    if amount > 100000000:
        return True
    else :
        return False

#in tabe baraye barresi tedad bardasht ha ast ke agar bishtar az 3 bood yanbi mashkook ast
def check_repeated_withdrawals(withdraw_count):
    if withdraw_count > 3:
        return True
    else :
        return False

#in tabe baraye barresi mablaghe mojoodie ke aya mablagh bardasht bishtar az mojoodi ast ya na 
def check_balance(balance, amount):
    if amount > balance:
        return True
    else :
        return False

#tabe baraye tolid list az gozaresh mashkook ast ke ba teb haye dige barresi shode 
def generate_fraud_report(username, transaction_type, amount, time, reasons):
    return {
        'username': username,
        'type': transaction_type,
        'amount': amount,
        'time': time,
        'reasons': reasons
    }

#tabe asli barresi
def detect_fraud(transactions):
    balances = {}
    withdraw_counts = {}
    suspicious_transactions = []

#tabe baraye barresi tak take tarakonesh ha 
    for username, transaction_type, amount, time in transactions:
        if username not in balances:
            balances[username] = 0
            withdraw_counts[username] = 0

        reasons = []

    #barresi mablaghe tarakonesh ba estefade az tabe large transaction ke agar balaye 100 bood be dalil ezafe kone 
        if check_large_transaction(amount):
            reasons.append('Large transaction')
        
        #barresi noe tarakonesh bardasht ast ya na 
        if transaction_type == 'withdraw':
            #barresi mojoodi ba mablaghe bardasht
            if check_balance(balances[username], amount):
                reasons.append('Withdraw is more than balance')

            withdraw_counts[username] += 1

            #barresi tedad bardasht ke bishatr az 3 ast yana 
            if check_repeated_withdrawals(withdraw_counts[username]):
                reasons.append('More than 3 repeated withdrawals')

            balances[username] -= amount

        elif transaction_type == 'deposit':
            balances[username] += amount

        
            withdraw_counts[username] = 0
        #age reason khali nabashe yani mashkook boode 
        if reasons:
            #ba tabe generate fraud report  gozareshe tarakonesh mashkook misazim
            report = generate_fraud_report(
                username,
                transaction_type,
                amount,
                time,
                reasons
            )
            
            #ezafe kardan gozaresh be list mashkook
            suspicious_transactions.append(report)

    return suspicious_transactions


transactions = [
    ('Ali', 'deposit', 50000000, 10),
    ('Ali', 'withdraw', 2000000, 11),
    ('Ali', 'withdraw', 3000000, 12),
    ('Ali', 'withdraw', 4000000, 13),
    ('Ali', 'withdraw', 5000000, 14),
    ('Ali', 'withdraw', 6000000, 15),
    ('Sara', 'deposit', 50000000, 20),
    ('Sara', 'withdraw', 60000000, 21),
    ('Reza', 'deposit', 150000000, 30)
]

result = detect_fraud(transactions)
#barresi tat take tarakonesh ha va chape etelaate khaste shode 
for transaction in result:
    print('Username:', transaction['username'])
    print('Type:', transaction['type'])
    print('Amount:', transaction['amount'])
    print('Time:', transaction['time'])
    print('Reasons:', transaction['reasons'])
    print('--------------------')