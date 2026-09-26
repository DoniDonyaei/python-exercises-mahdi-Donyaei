#moteghayer baraye zakhire 
FILE_NAME = 'users.txt'

#tabe baraye voroodi karbara
def find_user(username):
    #ba r baz mikonim file ro ke faghat bekhoone
    file = open(FILE_NAME, 'r')
#ye loop baraye in ke khat be khat file ro bekhoone
    for line in file:
        user = line.strip().split(',')
        
        #barresi mikone name karbari too file ba name karbari voroodi yeki bashe
        if user[0] == username:
            print('کاربر پیدا شد:', line.strip())
            #age yeki bood print mikone o mibande
            file.close()
            return True
    #halghe tamoom shode karbar peyda nashode pas bar migardoone False
    print('کاربر پیدا نشد.')
    file.close()
    return False

#tabe baraye add kardan karbar jadid 
def add_user(username, password, status='active'):
    
    #tabe find ro seda mizanim ke barresi kone username az ghabl vojood dare ya na 
    if find_user(username):
        print('این username قبلاً وجود دارد.')
        return
#file ro a baz mikonim ke mikhaym ezafe konim be akhare file 
    file = open(FILE_NAME, 'a')
    #etelaate karbar jadid inja neveshte mishe 
    file.write(username + ',' + password + ',' + status + '\n')
    file.close()

    print('کاربر اضافه شد.')

#tabe hazf kardan karbar 
def delete_user(username):
    
    #file ba r baz mikonim baraye khoondan file 
    file = open(FILE_NAME, 'r')
    lines = file.readlines()
    file.close()

    #filw ro ba w baz mikonim(write) info ghabli pak mishe intori va info jadid neveshte mishe 
    file = open(FILE_NAME, 'w')
    #moteghayer baraye  in ke bedoonim user peyda shode va hazf shode ya na 
    found = False
    
    #loop baraye barresi hameye line haye zakhire shode 
    for line in lines:
        user = line.strip().split(',')
        
        #barresi karbari ke mikhaym hazf konim
        if user[0] == username:
            #age karbar peyda she pas shart True mishe ,dobare nevshte nemishe in khat pas hazf mishe karbar 
            found = True
            
        #age peyda nashod karbar pas dobare neveshte mishe oon line     
        else:
            file.write(line)

    file.close()

    if found:
        print('کاربر حذف شد.')
    else:
        print('کاربر پیدا نشد.')

#tabe baraye gozaresh
def generate_report():
    #file ba r baz mishe takhoonde she 
    file = open(FILE_NAME, 'r')
    
    #2ta counter baraye karbare active va block shode 
    active_count = 0
    blocked_count = 0

    #loop baraye barresi khat be khat
    for line in file:
        #joda kardane etelaate karbar 
        user = line.strip().split(',')

        if user[2] == 'active':
            active_count += 1

        if user[2] == 'blocked':
            blocked_count += 1

    file.close()

    print('تعداد کاربران فعال:', active_count)
    print('تعداد کاربران مسدود:', blocked_count)

generate_report()