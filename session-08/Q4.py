#tabe baraye daryaft meghdar 
def get_values():
    #list misaze baraye zakhire meghdar 
    values = []

    #az karbar meghdaro migire o int tabdil mikone 
    count = int(input('تعداد مقادیر: '))
    #be tedad count ke karbar vared karde halghe doros mikone 
    for i in range(count):
        #har bar ke ejra mishe meghdar migire 
        value = input('مقدار را وارد کنید: ')
        #barreessi mikone ke khali vared shode ya na 
        if value == '':
            print('مقدار خالی اضافه نشد.')
        #age khali nabashe be lsit value ezafe mikone 
        else:
            values.append(value)

    return values

#tabe baraye barresi inke meghdar jadid ast ya na 
def add_unique(value, unique_values):
    #tamame list unique ro barresi mikone 
    for i in range(len(unique_values)):
        #ba lower hame horoof ro koochik mikonim tebghe khasteye soal
        if value.lower() == unique_values[i].lower():
            return i + 1

    unique_values.append(value)
    return 0

#tabe baraye barresi maghadir vared shode 
def process_values(values):
    #3ta list khali misazim baraye zakhire 
    unique_values = []
    duplicate_values = []
    first_positions = []

    #barresi meghdar haye vared shode 
    for value in values:
        position = add_unique(value, unique_values)
        
        #barresi mikone tekrari boode meghdar ya na 
        if position != 0:
            #age bood too list tekrari zakhire mishe 
            duplicate_values.append(value)
            #avalin voroodie 
            first_positions.append(position)
    #har 3 taro barmigardoone baraye estefade mojadad
    return unique_values, duplicate_values, first_positions

#tabe baraye gozaresh
def show_report():
    values = get_values()

    unique_values, duplicate_values, first_positions = process_values(values)

    print('لیست مقادیر unique:', unique_values)
    print('تعداد مقادیر unique:', len(unique_values))
    print('تعداد مقادیر تکراری:', len(duplicate_values))
    #loop baraye barresi tekrar 
    for i in range(len(duplicate_values)):
        print(
            'مقدار تکراری:',
            duplicate_values[i],
            '- اولین بار در موقعیت',
            first_positions[i],
            'وارد شده است.'
        )
        
show_report()