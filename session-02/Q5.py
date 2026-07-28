#barnamei benevisid ke masafat tey shode bar hasb KM az karbar daryaft konad agar masafat kamtar az 2km bood keraye sabet 20.000 toman bashad dar gheyre insoorat be ezaye har km ezafe 5.000 toman azafe shavad 
#dar payan keraye nahaei ra chap konid  

distance = float ( input (" مسافت طی شده را بر حسب کیلومتر وارد کنید : "))
if distance <= 2:
    cabfee = 20000
    print('کرایه شما ',cabfee,'تومان است')
else:
    cabfee = 20000 +(distance-2)*5000
    print('کرایه شما ',cabfee,'تومان است')
    