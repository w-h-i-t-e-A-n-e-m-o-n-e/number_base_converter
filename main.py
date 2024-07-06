def convert():
    ns_from = combobox_from.get()
    ns_to = combobox_to.get()
    number = ent_number.get()
    if ns_from == '' or ns_to == '' or number == '':
        lbl_result['text'] = 'Выберите системы счисления для перевода и введите число'
    elif ns_from == 'Двоичная':
        try:
            converted_number = int(number, 2)
            if ns_to == 'Восьмеричная':
                result = oct(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2082 = {result}\u2088'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Десятичная':
                result = converted_number
                lbl_result['text'] = f'{number}\u2082 = {result}\u2081\u2080'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Шестнадцатеричная':
                result = hex(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2082 = {result}\u2081\u2086'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            else:
                lbl_result['text'] = 'Системы счисления одинаковы'
        except ValueError:
            lbl_result['text'] = 'Невозможно сделать перевод'

    elif ns_from == 'Восьмеричная':
        try:
            converted_number = int(number, 8)
            if ns_to == 'Двоичная':
                result = bin(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2088 = {result}\u2082'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Десятичная':
                result = converted_number
                lbl_result['text'] = f'{number}\u2088 = {result}\u2081\u2080'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Шестнадцатеричная':
                result = hex(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2088 = {result}\u2081\u2086'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            else:
                lbl_result['text'] = 'Системы счисления одинаковы'
        except ValueError:
            lbl_result['text'] = 'Невозможно сделать перевод'

    elif ns_from == 'Десятичная':
        try:
            converted_number = int(number)
            if ns_to == 'Двоичная':
                result = bin(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2081\u2080 = {result}\u2082'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Восьмеричная':
                result = oct(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2081\u2080 = {result}\u2088'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Шестнадцатеричная':
                result = hex(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2081\u2080 = {result}\u2081\u2086'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            else:
                lbl_result['text'] = 'Системы счисления одинаковы'
        except ValueError:
            lbl_result['text'] = 'Невозможно сделать перевод'

    elif ns_from == 'Шестнадцатеричная':
        try:
            converted_number = int(number, 16)
            if ns_to == 'Двоичная':
                result = bin(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2081\u2086 = {result}\u2082'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Восьмеричная':
                result = oct(converted_number)[2:]
                lbl_result['text'] = f'{number}\u2081\u2086 = {result}\u2088'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            elif ns_to == 'Десятичная':
                result = converted_number
                lbl_result['text'] = f'{number}\u2081\u2086 = {result}\u2081\u2080'
                cursor.execute(f"""INSERT INTO conversion VALUES ('{ns_from}', '{converted_number}', '{ns_to}', '{result}')""")
                db.commit()
            else:
                lbl_result['text'] = 'Системы счисления одинаковы'
        except ValueError:
            lbl_result['text'] = 'Невозможно сделать перевод'


def analize():
    list_from = []
    list_to = []
    list_from_count = []
    list_to_count = []
    for entry in cursor.execute('SELECT * FROM conversion'):
        print(entry)
        list_from.append(entry[0])
        list_to.append(entry[2])
    for item in numeral_system:
        list_from_count.append(list_from.count(item))
        list_to_count.append(list_to.count(item))
        print(item)
    print(list_from_count)
    print(list_to_count)
    height = 0.4
    y_indexes = np.arange(4)

    plt.figure()

    plt.subplot()
    plt.title('Количество переводов')
    plt.yticks(y_indexes, ['2', '8', '10', '16'])
    plt.xlabel('Число переводов')
    plt.ylabel('Система счисления')
    plt.barh(y_indexes - (height/2), list_from_count, color='b', label='Из', height=height)
    plt.barh(y_indexes + (height/2), list_to_count, color='r', label='В', height=height)
    plt.legend()

    plt.show()


from tkinter import *
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

db = sqlite3.connect('server.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS conversion (
            from_numeral_system TEXT,
            number TEXT,
            to_numeral_system TEXT,
            result TEXT
        )''')
db.commit()

# cursor.execute('drop table conversion')
# db.commit()

root_main = Tk()

root_main.title('Перевод систем счисления')
# root_main.geometry('1000x600')
root_main.resizable(width=False, height=False)
root_main['bg'] = 'lightblue'

lbl_header = Label(root_main, text="Перевод систем счисления", bg='lightblue', fg="black", font="Consolas 30")
lbl_from = Label(root_main, text="Из какой", bg='lightblue', fg="black", font="Consolas 20")
lbl_number = Label(root_main, text="Число для перевода:", bg='lightblue', fg="black", font="Consolas 20")
lbl_to = Label(root_main, text="В какую", bg='lightblue', fg="black", font="Consolas 20")
lbl_result = Label(root_main, bg='lightblue', fg="black", font="Consolas 20")

ent_number = Entry(root_main, font="Consolas 20", justify="center", cursor='pencil')

lbl_header.grid(column=0, row=0, columnspan=3, pady=30)
lbl_from.grid(column=0, row=1)
lbl_number.grid(column=1, row=1, padx=50, pady=30)
lbl_to.grid(column=2, row=1)
ent_number.grid(column=1, row=2)

numeral_system = ['Двоичная', 'Восьмеричная', 'Десятичная', 'Шестнадцатеричная']
combobox_from = ttk.Combobox(values=numeral_system)
combobox_to = ttk.Combobox(values=numeral_system)
combobox_from.grid(column=0, row=2, padx=30)
combobox_to.grid(column=2, row=2, padx=30)

btn_convert = Button(root_main, text='Перевести', bg='#001561', fg='#FFFFFF', font='Consolas 24', cursor='spider',
                     command=convert)
btn_analyze = Button(root_main, text='Анализ', bg='#001561', fg='#FFFFFF', font='Consolas 24', command=analize)

btn_convert.grid(column=1, row=3, pady=30)
lbl_result.grid(column=0, row=4, columnspan=3, pady=30)
btn_analyze.grid(column=2, row=5, pady=30)

root_main.mainloop()
