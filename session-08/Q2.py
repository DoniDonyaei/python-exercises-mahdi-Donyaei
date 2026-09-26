#moteghayer 
FILE_NAME = 'logs.txt'


#tabe baraye hesab kardan log in movafagh
def count_successful_logins():
    
    #ba r baz mikonim ke faghat khoonde she 
    file = open(FILE_NAME, 'r')
    count = 0

    #loop baraye khat be khat khandane code 
    for line in file:
        #har khat ro joda mikone 
        log = line.strip().split(',')
        #sharte vorood movafagh ro barresi mikone va agar movafagh bood shomarande yeki ezafe mishe 
        if log[1] == 'LOGIN' and log[2] == '200':
            count += 1

    file.close()
    #tedad vorood movafagh ro mide 
    return count

#tabe baraye vorood haye na movafagh
def count_failed_logins():
    file = open(FILE_NAME, 'r')
    count = 0

    for line in file:
        log = line.strip().split(',')

        #barresi mikone age 200 nabashe pas vorood NAmovafagh boode va yeki be shomarande ezafe mikone 
        if log[1] == 'LOGIN' and log[2] != '200':
            count += 1

    file.close()
    #tedad vorood namovafgh ro mide 
    return count

#tabe baraye peyda kardane karbare mashkook
def find_suspicious_users():
    #faile baz mikone list khali misaze be esme Eror ke karbar ba khataye 403 too oon zakhire she 
    file = open(FILE_NAME, 'r')
    errors = []

    #loop baraye baresi khat be khat 
    for line in file:
        log = line.strip().split(',')
        
        #barresi ke aya code 403 ast ya kheyr
        if log[2] == '403':
            #age 403 bood be list erroe ezafe mishe 
            errors.append(log[0])

    file.close()

    #list khali misaze ta har user yekbar barresi she 
    checked_users = []

    #loop baraye barresi user ha too list error 
    for username in errors:
        #sharte barresi in ke karbar ghablan barresi shode ya na 
        if username not in checked_users:
            #age barresi nashode bashe ezafe mishe be list 
            checked_users.append(username)

            #tedad esm karbar ke too list error hast ro mishmare age 3khataye 403 dashte bashe yani mashkooke
            if errors.count(username) >= 3:
                print(username)

#tabe baraye gozaresh nahaei
def generate_report():
    print('تعداد Login موفق:', count_successful_logins())
    print('تعداد Login ناموفق:', count_failed_logins())

    print('کاربران مشکوک:')
    find_suspicious_users()

    file = open(FILE_NAME, 'r')
    users = []

    for line in file:
        log = line.strip().split(',')

        if log[0] not in users:
            users.append(log[0])

    file.close()

    print('تعداد عملیات هر کاربر : ')

    for username in users:
        file = open(FILE_NAME, 'r')
        operation_count = 0

        for line in file:
            log = line.strip().split(',')

            if log[0] == username:
                operation_count += 1

        file.close()

        print(username, ':', operation_count)

generate_report()