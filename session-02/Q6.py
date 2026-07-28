#mablaghe kharid ra az karbar daryaft konid va tebghe sharayet takhfif ra mohasebe konid 
#bishtar az 1m kharid ---> 15%
#500.000 ta 1m kharid --->10%
#kamtar az 500.000 --->0%

tottal_amount = float(input('مبلغ کل خرید را وارد کنید : '))
if tottal_amount >= 1000000:
    discount = tottal_amount * 0.15
    
elif tottal_amount >= 500000:
    discount = tottal_amount * 0.10
    
else:
    discount = 0
finalprice = tottal_amount - discount

print('مبلغ قابل پرداخت شما :',finalprice , 'میباشد')