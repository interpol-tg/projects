# баланс

# ввод, вывод средств
import time
import tkinter as tk
from tkinter import scrolledtext
import codecs


balans = 0
def zapros():
    poluch = txt.get()
    print(poluch)
    if poluch == 'admin':
        admin()
        txt.delete(0, tk.END)

    elif poluch == '1234':
        client()
        txt.delete(0, tk.END)


def deposit_money():
    global poluch
    lbl.configure(text="Введите сумму для пополнения: ")
    txt.place(x=260, y=150)
    btn.configure(text="Пополнить", command=sum_balans)
    lbl.place(x=240, y=130)
    btn.place(x=260, y=180)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    txt_ent1.place(x=100000, y=100000)
    text_1 = codecs.open("deposit.txt", "a+", "utf-8")
    local_time = time.ctime()
    # text_1.write(f"\nПополнения: {poluch}\n{local_time}")
    # text_1.write("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def sum_balans():
    global balans
    poluch = txt.get()
    balans = int(balans) + int(poluch)
    lbl.configure(text="Готово!")
    lbl.place(x=260, y=150)
    btn.configure(text="Вернуться", command=client)
    txt_ent.place(x=100000, y=100000)
    txt_ent1.place(x=100000, y=100000)
    print(balans)


def cash_get():
    lbl.configure(text="Введите сумму для снятия: ")
    txt.place(x=260, y=150)
    poluch = txt.get()
    print(poluch)
    btn.configure("Снять", command=check)
    lbl.place(x=260, y=130)
    btn.place(x=260, y=170)
    btn1.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)


def check():
    global balans
    if int(balans) > int(poluch):
        balans = eval(f'{a} - {poluch}')
        text_2 = codecs.open("get_money.txt", "a+", "utf-8")
        local_time = time.ctime()
        text_2.write(f"\nСнятие наличных: {poluch}\n{local_time}")
        text_2.write("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        lbl.configure(text="Готово!")
        btn.configure("Назад", command=client)
        lbl.place(x=260, y=150)
        btn.place(x=260, y=170)

    else:
        lbl.configure(text="У вас недостаточно средств.")
        btn.configure("Назад", command=client)
        lbl.place(x=260, y=150)
        btn.place(x=260, y=170)


def end_operations():
    lbl.configure(text="Досвидания!")
    lbl.place(x=260, y=150)
    btn.place(x=1000000, y=1000000)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)


def check_balans():
    lbl.configure(text=f"Ваш баланс: {balans}")
    btn.configure(text="Назад", command=client)
    lbl.place(x=225, y=130)
    btn.place(x=225, y=170)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)


def client():
    btn.configure(text='Внести наличные', command=deposit_money)
    btn1.configure(text='Снять наличные', command=cash_get)
    btn2.configure(text='Завершить операцию', command=end_operations)
    btn3.configure(text='Проверить баланс', command=check_balans)

    btn.place(x=225, y=170)
    btn1.place(x=225, y=210)
    btn2.place(x=225, y=250)
    btn3.place(x=225, y=130)
    txt.place(x=10000, y=10000)
    txt_ent.place(x=10000, y=10000)
    lbl.place(x=10000, y=10000)


def admin():
    btn.configure(text='Просмотр логов пополнения', command=admin_panel_1)
    btn1.configure(text='Просмотр логов снятия', command=admin_panel_2)
    btn2.configure(text='Обзор и загрузка купюр', command=admin_panel_3)
    btn3.configure(text='Назад', command=pincode)
    txt.place(x=10000, y=10000)
    btn.place(x=210, y=130)
    btn1.place(x=225, y=170)
    btn2.place(x=225, y=210)
    btn3.place(x=10, y=10)
    txt1.place(x=1000000, y=1000000)
    txt2.place(x=1000000, y=1000000)
    txt3.place(x=1000000, y=1000000)


def admin_panel_1():
    txt1.place(x=100, y=75)
    btn.configure(text='Назад', command=admin)
    btn.place(x=10, y=10)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    with codecs.open('deposit.txt', 'r+', 'utf-8') as f:
        line = f.read()
        txt1.insert('1.0', line)


def admin_panel_2():
    txt2.place(x=100, y=75)
    btn.configure(text='Назад', command=admin)
    btn.place(x=10, y=10)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    with codecs.open('get_money.txt', 'r+', 'utf-8') as f:
        line = f.read()
        txt2.insert('1.0', line)


def admin_panel_3():
    txt3.place(x=100, y=75)
    btn.configure(text='Назад', command=admin)
    btn.place(x=10, y=10)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    with codecs.open('Var_money.txt', 'r+', 'utf-8') as f:
        line = f.read()
        txt3.insert('1.0', line)


def pincode():
    txt.place(x=260, y=130)
    btn.configure(text="Принять", command=zapros)
    btn.place(x=262, y=160)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)


win = tk.Tk()
win.title("BANKOMAT")
win.geometry('600x400')
lbl = tk.Label(win)
lbl1 = tk.Label(win)
txt = tk.Entry(win, width=10, justify="center")
txt_ent = tk.Entry(win, width=10, justify="center")
txt_ent1 = tk.Entry(win, width=10, justify="center")
txt1 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
txt2 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
txt3 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
btn = tk.Button(win, text="Начать", command=pincode)
btn1 = tk.Button(win)
btn2 = tk.Button(win)
btn3 = tk.Button(win)
btn.place(x=260, y=150)
win.mainloop()
