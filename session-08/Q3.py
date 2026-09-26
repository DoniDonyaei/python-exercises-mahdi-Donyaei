#esme file asli va moteghayer 
FILE_NAME = 'transactions.txt'

#tabe baraye barresi mojoodi karbar 
def calculate_balance(username):
    #file ro baz mikone va mikhoone ba 'r'
    file = open(FILE_NAME, 'r')
    #mojoodi avalie ro 0 dar nazar migirim
    balance = 0
    
    #tabe baraye khoondan khat be khat 
    for line in file:
        transaction = line.strip().split(',')
        
        #barresi mikone tarakonesh marboot be user hast ya na 
        if transaction[0] == username:
            #mablagh be int tabdil mishe 
            amount = int(transaction[2])
            
            #age noe tarakonesh deposit bashe be mojoodi ezafe mishe 
            if transaction[1] == 'deposit':
                balance += amount
            
            #barresi mikone noe tarakonesh withdra ast ya na 
            if transaction[1] == 'withdraw':
                #age mablagh bardasht kamtar ya mosavi mojoodi bashe tarakonesh anjam mishe va az mojoodi kam mishe
                if amount <= balance:
                    balance -= amount

    file.close()
    #mojoodi nahaei bade amaliat ro neshoion mide
    return balance

#tabe baraye majmooe deposit 
def total_deposits(username):
    file = open(FILE_NAME, 'r')
    #majmooe deposit 0 dar nazar gerefte mishe 
    total = 0

    for line in file:
        transaction = line.strip().split(',')
        
        #barresi inke tarakonesh marboot be karbar bashe 
        if transaction[0] == username:
            #age tarakonesh deposit bashe mablagh be majmoo ezafe mishe 
            if transaction[1] == 'deposit':
                total += int(transaction[2])

    file.close()
    return total


#tabe baraye majmooe bardasht 
def total_withdrawals(username):
    file = open(FILE_NAME, 'r')
    #majmooe bardasht 0 dar nazar gerefte mishe 
    total = 0

    for line in file:
        transaction = line.strip().split(',')
        
        #barresi in ke tarakonesh marboot be karbar ast
        if transaction[0] == username:
            #age tarakonesh bardasht bashe be majmooe bardasht ezafe mishe 
            if transaction[1] == 'withdraw':
                total += int(transaction[2])

    file.close()
    return total

#tabe baraye barresi bardasht na motabar 
def find_invalid_transactions(username):
    file = open(FILE_NAME, 'r')
    #mojoodi 0 dar nazar gertefte mishe 
    balance = 0
    #list khali misaze baraye tarakoneshe na motabar 
    invalid_transactions = []

    for line in file:
        transaction = line.strip().split(',')

        #barresi tarakonesh karbar 
        if transaction[0] == username:
            amount = int(transaction[2])

            #age deposit bashe be mojoodi ezafe mishe 
            if transaction[1] == 'deposit':
                balance += amount
            
            #age bardasht bashe sharte jadid barresi mishe 
            if transaction[1] == 'withdraw':
                #age mablaghe bardasht az mojoodi bishtar bashe  tarakonesh na motabar mishe 
                if amount > balance:
                    invalid_transactions.append(line.strip())
                    
                #dar gheyre in soorat  bardasht anjam mishe o mablagh az mojoodi kam mishe 
                else:
                    balance -= amount

    file.close()
    #tarakonesh na motabar ro bar migardoone
    return invalid_transactions

#tabe baraye gozaresh
def generate_report():
    file = open(FILE_NAME, 'r')
    #list khali baraye esm  karbara misaze 
    users = []

    for line in file:
        transaction = line.strip().split(',')
        
        #age nam karbar too list naboode oon ro ezafe mikone 
        if transaction[0] not in users:
            users.append(transaction[0])

    file.close()
    
    #loop baraye barresi yek be yek karbara
    for username in users:
        print('نام:', username)
        print('مجموع واریز:', total_deposits(username))
        print('مجموع برداشت:', total_withdrawals(username))
        print('موجودی:', calculate_balance(username))

        invalid_transactions = find_invalid_transactions(username)

        print('تراکنش‌های نامعتبر:')

        if len(invalid_transactions) == 0:
            print('ندارد')
        else:
            for transaction in invalid_transactions:
                print(transaction)

        
            
            
generate_report()