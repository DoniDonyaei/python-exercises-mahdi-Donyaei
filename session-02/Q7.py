#shomare card 16 raghami ra be soorat reshte az karbar daryaft konid speas 4 raghame aval ra joda karde va barresi konid ba shomare moshakhas shode 6037 motabeghat darad ya kheyr
#dar soorat tatabogh nam bank farzi ra namayesh dahid dar gheyre in soorat payam monaseb namayesh dahid 

cardnumber = input (' شماره کارت بانکی خود را وارد کنید : ')
bankcode = cardnumber[:4]

if bankcode =='6037':
    print('بانک شما ملی است')
else:
    print('شماره وارد شده صحیح نمیباشد لطفا مجدد بررسی کنید')
