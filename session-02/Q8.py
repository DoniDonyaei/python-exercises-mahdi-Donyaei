#adadi beyne 0 ta 23 az karbar daryaft konid va baze zamani rooz ra moshakhas konid (sobh,zohr,asr,shab)
#agar adad vared shode az baze kharej bood payam khat chap konid 

hour =float(input(' ساعت مد نظر خود را وارد کنید : '))
if hour< 12:
    print('صبح')
elif hour < 17 :
    print('ظهر')
elif hour < 19 :
    print('عصر')
elif hour < 23 :
    print('شب')
else:
    print('لطفا عدد را به درستی وارد کنید')