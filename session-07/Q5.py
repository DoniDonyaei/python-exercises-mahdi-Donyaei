#daryaft list log 
def analyze_logs(logs):
    result = {}
    
    #moteghayer baraye shemordane login movafagh va na movafagh
    successful_logins = 0
    failed_logins = 0

    #barresi tak tak log ha 
    for username, action, status in logs:
        if username not in result:
            result[username] = {
                'operations': 0,
                'failed_403': 0,
                'suspicious': False
            }

   #baraye har log yeki be tedad ezafe mikonim
        result[username]['operations'] += 1

        #agar vaziat 200 bood yani movafagh
        if action == 'LOGIN' and status == 200:
            successful_logins += 1

        #agar vaziat 200 nabood yani failed 
        elif action == 'LOGIN' and status != 200:
            failed_logins += 1

       #barresi vaziat 403 ke yani khata (failed )
        if status == 403:
            result[username]['failed_403'] += 1

   #list baraye karbare mashkook
    suspicious_users = []

#loop baraye barresi karbarane list result . agar 403 bood True mikonim javabo va ezafe mikonim be list suspicious(mashkook)
    for username in result:
        if result[username]['failed_403'] >= 3:
            result[username]['suspicious'] = True
            suspicious_users.append(username)
    
    
    #javabi ke dar enteha bayad bargardoone 
    return {
        'successful_logins': successful_logins,
        'failed_logins': failed_logins,
        'users': result,
        'suspicious_users': suspicious_users
    }

#etelaate dade shode be ma 
logs = [
    ('Ali', 'LOGIN', 200),
    ('Ali', 'DOWNLOAD', 200),
    ('Sara', 'LOGIN', 403),
    ('Reza', 'LOGIN', 200),
    ('Sara', 'LOGIN', 403),
    ('Sara', 'LOGIN', 403)
]

#tabe ro seda mikonim ke ejra she ba etelaat jadid dade shode 
answer = analyze_logs(logs)

#tedade  vorood movafagh(code 200 ) va na movafagh(code 403) va karbare mashkook
print('Successful logins:', answer['successful_logins'])
print('Failed logins:', answer['failed_logins'])
print('Suspicious users:', answer['suspicious_users'])
print('--------------------')

#har karbar jodagane barresi mishe ba in loop va nam karbar va  tedad amaliat va tedad khata  va karbare mashkook(3khata va bishtar )ra print mikonim
for username, info in answer['users'].items():
    print('Username:', username)
    print('Operations:', info['operations'])
    print('403 errors:', info['failed_403'])
    print('Suspicious:', info['suspicious'])
    print('--------------------')