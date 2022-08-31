import webbrowser
from tkinter import *
from tkinter import messagebox
import win32com.client as win32
import time
import os
import tkinter as tk
from tkinter import ttk
import pyperclip
import pyautogui
import pymouse,pykeyboard,os,sys
from pymouse import *
#from pykeyboard import PyKeyboard
import json
import codecs
import shutil
from PIL import ImageTk, Image
import logging


logging.basicConfig(filename='example.log', level=logging.DEBUG)

f = open('text.txt', 'rt')
# Сформировать новый список
lst = [] # сначала пустой список
# Реализовать обход файла по строкам и считать числа.
# Для чтения строк используется итератор файла.
for s in f:
    # Убрать последний символ '\n' из s
    s = s.rstrip()

    # Вывести s для контроля
    # print(s)

    # Добавить строку s в список lst
    lst = lst + [s]
logging.info('Письмо отправлено')
f.close()


colorl = lst[5]
b0 = lst[0]
b1 = lst[1]
b2 = lst[2]
b3 = lst[3]
b4 = lst[4]
cc = lst[6]
color2 = lst[7]
color3 = lst[8]
color4 = lst[9]

def Them():
    app = Tk()
    app.title("Настройки")
    # colorl = '#FFFBF0'
    # app['background'] = colorl    
    app.geometry('250x100')
    app['background'] = colorl
    labelTop = Label(app, text = "Тема", fg=color2, bg=colorl)
    
    labelTop.grid(column=0, row=0)
    comboExample = ttk.Combobox(app, values=["Светлая", "Темная"], width=9)
    comboExample.grid(column=0, row=1, padx=7, pady=10)

    
    # comboExample.current(cc)
    if cc == 'light':
        comboExample.current(0)
    elif cc == 'dark':
        comboExample.current(1)
    # labelExample1 = Label(app, text="Customized Color",bg='red', fg=colorl)
    # labelExample1.grid(column=0, row=2)
    
    def callbackFunc(event):
        global colorl
        global b0
        global b1
        global b2
        global b3
        global b4
        
        if comboExample.get() == "Светлая":
            colorl=lst[5]
            lst[5] = '#FFFBF0'
            lst[0] = 'button_gtp-bia.png'
            lst[1] = 'button_gpp-bia.png'
            lst[2] = 'button_monitoring.png'
            lst[3] = 'button_ochistit.png'
            lst[4] = 'button_otpravit.png'
            lst[6] = 'light'
            lst[7] = '#242f3d'
            lst[8] = '#FFFFFF'
            lst[9] = lst[8]
            f = open('text.txt', 'wt')
            for s in lst:
                # записать каждую строку в отдельную строку файла
                f.write(s + '\n')
            f.close()
            
       
        elif comboExample.get() == "Темная":
            lst[5] = '#242f3d'
            lst[0] = 'button_gtp-bia (1).png'
            lst[1] = 'button_gpp-bia (1).png'
            lst[2] = 'button_monitoring-bia (1).png'
            lst[3] = 'button_ochistit (1).png'
            lst[4] = 'button_otpravit (1).png'
            lst[6] = 'dark'
            lst[7] = '#FFFBF0'
            lst[8] = '#000000'
            lst[9] = '#696969'
            f = open('text.txt', 'wt')
            for s in lst:
                # записать каждую строку в отдельную строку файла
                f.write(s + '\n')
            f.close()
            
                                  
    comboExample.bind("<<ComboboxSelected>>", callbackFunc)
    
    def bgBlack():
        root.destroy()
        app.destroy()
        os.startfile("C:\python\mail_2.py")
            
    
    button_select = Button(app,text="Применить", command=bgBlack, fg=colorl, bg=color2) 
    button_select.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    # def selection():

    
    # labelValue = Label(app, textvariable=radioValue)
    # labelValue.grid(column=2, row=0, sticky="E", padx=40)
    app.mainloop()
           
def export():
    shutil.copyfile(r'.\bkp\filestrs111.txt', r'filestrs111.txt')
    shutil.copyfile(r'.\bkp\text.txt', r'text.txt')
def update():
    messagebox.showinfo("Обновление", "Обновление не доступно для данной версии программы")
def helpi():
     webbrowser.open_new("https://www.google.com/") #Ссылка на Инструкцию по Эскалации
def about():
    a = Toplevel()
    w = a.winfo_screenwidth()
    h = a.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    a.geometry('300x170'.format(w, h))
    a.resizable(width=False, height=False)
    a.wm_attributes('-transparentcolor', colorl)
    a.title("О программе")
    a['bg'] = colorl
    label1 = Label(a, text = "Здесь должна быть информация. о программе...", fg=color2, bg=colorl)
    label1.pack()
    poetry = "\nНо..., мне лень печатать и вот Вам Гёте:\n\nВот мысль, которой весь я предан,\nИтог всего, что ум скопил.\nЛишь тот, кем бой за жизнь изведан,\nЖизнь и свободу заслужил."
    label2 = Label(a, text=poetry, justify=LEFT, fg=color2, bg=colorl)
    label2.place(relx=.10, rely=.1)
    a.overrideredirect(False)
def bia1():
    surname_entry.delete(0, END)
    surname_entry.insert(0, "")
def bia2():
    surname_entry.delete(0, END)
    surname_entry.insert(0, "")
def bia3():
   surname_entry.delete(0, END)
   surname_entry.insert(0, "")
def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
def select():
    l = stat.get()
    if l == 1:
        sel.config(text="Срочности", bg=colorl, font=("Pagella", 9, 'bold'))
    elif l == 2:
        sel.config(text="Статусу", bg=colorl, font=("Pagella", 9, 'bold'))
def addrbook():
    adr = Tk()
    adr.title("Дерьмо")
    adr.geometry("300x100")
    adr['background'] = colorl
    f1 = open('filestrs111.txt', 'rt') #encoding="utf-8"
    # 6. Сформировать новый список
    lst21 = []
    # сначала пустой список

    # 7. Реализовать обход файла по строкам и считать числа.
    # Для чтения строк используется итератор файла.
    for s1 in f1:
        # Убрать последний символ '\n' из s
        s1 = s1.rstrip()

        # Вывести s для контроля
        # print(s)

        # Добавить строку s в список lst2
        lst21 = lst21 + [s1]

    # 8. Вывести список lst2 для контроля
    #print(lst2[2])
    lst21_len = len(lst21)
    i1=0
    lst1 = []
    while i1 < lst21_len:
        global y1
        g1 = lst21[i1]
        i1 += 1
        y1 = g1.rpartition(';')[0]
        lst1.append(y1)
        
    def qwer():
        p1 = comboExample.get()
        u1 = lst21
        for x1 in iter(u1):
            if p1 in x1:
                o1 = x1.rpartition(';')[-1]
                surname_entry.delete(0, END)
                surname_entry.insert(0, o1)
                adr.destroy()

    def add(): # Добавление записи
        add3 = tk.Tk()
        add3.title("Добавление записи")
        add3.geometry("400x150")
        add3['background'] = colorl
        add3.attributes("-topmost", True)
        def add4():
            name2 = str(name_entry2.get()) 
            surname2 = str(surname_entry2.get())
           
            def match(surname2, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя"!#$%&\"/*+/=?^`{|}~" "\\')):
                return not alphabet.isdisjoint(surname2.lower())
            if name2 != 1:
                messagebox.showinfo("Ошибка ввода", "Введите корректный номер заявки!")
                add3.update()
            if match(surname2) == True:
                messagebox.showinfo("Ошибка ввода", "В адресе присутствуют некорректные символы!")
            elif "@" not in surname2:
                mentry.get()
            f2 = open('filestrs111.txt', 'a')  #encoding="utf-8"
            ott = str(name2 + ";" + surname2)
            f2.write('\n' + ott); 
            f2.close()
            add3.destroy()
          
        name2_label = Label(add3, text="Введите имя сотрудника:", padx=15, pady=10, font=("Pagella", 9, 'bold'), fg=color2, bg=colorl )
        surname2_label = Label(add3, text="Введите почту сотрудника:", padx=15, pady=10, font=("Pagella", 9, 'bold'), fg=color2, bg=colorl)
        
        name2_label.grid(row=0, column=0, sticky="w")
        surname2_label.grid(row=1, column=0, sticky="w")
        
        name_entry2 = Entry(add3, width=30, relief='solid')
        surname_entry2 = Entry(add3, width=30, relief='solid')
        
        name_entry2.grid(row=0,column=0, padx=180, pady=5, sticky="w")
        surname_entry2.grid(row=1,column=0, padx=200, pady=0, sticky="w")

        button_add2 = Button(add3, text="Добавить", command=add4, fg=color2, bg=colorl) 
        button_add2.grid(row=5, column=0, padx=150, pady=20, sticky="w")
               
        f1.close() 
        adr.destroy()
        add3.mainloop()


    def sort():
        try:
            file = open('filestrs111.txt', 'r+')
            pos = 0
            line = file.readlines()
            file.seek(pos)
            sort_text = sorted(line)
            for new_line in sort_text:
                file.write(new_line)
                pos = file.tell()
        except IOError:
            print("No such file or directory. Repeat, please!")    
        adr.update()
        file.close()
        adr.destroy()
        
    labelTop = Label(adr, text = "Выбери получателя", fg=color2, bg=colorl)
    labelTop.grid(column=0, row=0, sticky="w")
    comboExample = ttk.Combobox(adr, values=lst1, width=40)
    comboExample.grid(column=0, row=1, padx=5, pady=5, sticky="w")
    comboExample.current(1)
    
    button_select = Button(adr,text="Выбрать", command=qwer, fg=color2, bg=colorl) 
    button_select.grid(row=2, column=0, padx=10, pady=20, sticky="w")
    button_add = Button(adr,text="Добавить", command=add, fg=color2, bg=colorl) 
    button_add.grid(row=2, column=0, padx=120, pady=20, sticky="w")
    
    button_sort = Button(adr, text="Сортировать", command=sort, fg=color2, bg=colorl) 
    button_sort.grid(row=2, column=0, padx=200, pady=20, sticky="w")
    
    f1.close()
    adr.mainloop()
    
    
def copy():
    y = str(surname_entry.get())
    s = str(name_entry.get())
    x = len(s)
    if stat.get() == 1:
        es_type = 'срочности проведения работ.'
        es_work = 'провести работы по заявке БП Инцидент в первую очередь.'
    elif stat.get() == 2:
        es_type = 'непонятном статусе заявки.'
        es_work = 'предоставить заказчику информацию о текущем статусе по заявке в БП Инцидент со сроками выполнения.'
    else:
        sel.config(text="Статус не выбран!", foreground="red")
    def match(y, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя"!#$%&\"/*+/=?^`{|}~" "\\')):
        return not alphabet.isdisjoint(y.lower())
    if x != 9:
        messagebox.showinfo("Ошибка ввода", "Введите корректный номер заявки!")
        return
    elif s.isnumeric() == False:
        messagebox.showinfo("Ошибка ввода", "В номере заявки должны присутвовать только цифры")
        return
    elif match(y) == True:
        messagebox.showinfo("Ошибка ввода", "В адресе присутствуют некорректные символы!")
        return
    elif "@" not in y:
        mentry.get()
        return   
    isp = 'Исполнителя'
    body_text = ""
    body_text = body_text + 'Добрый день! \nПо заявке в БП Инцидент №' + name_entry.get() + ' от заказчика поступила эскалация, о ' + es_type
    body_text = body_text + 'Обращаем внимание ' + isp + ' о необходимости ' + es_work
    body_text = body_text + ""
    pyperclip.copy(body_text)
    result.config(text="Текс скопирован", font=("Pagella", 10, 'bold'), foreground="green", bg=colorl )
    result.after(5000, lambda: result.config(text=""))
    time.sleep(1)
    root.update() 
    
####################  для проверки шаблона 
def display():
    # body_text = ""
    # isp = 'Исполнителя'
    # y = str(surname_entry.get())
    # s = str(name_entry.get())
    # x = len(s)
    # if stat.get() == 1:
        # es_type = 'срочности проведения работ.'
        # es_work = 'провести работы по заявке БП Инцидент в первую очередь.'
    # elif stat.get() == 2:
        # es_type = 'непонятном статусе заявки.'
        # es_work = 'предоставить заказчику информацию о текущем статусе по заявке в БП Инцидент со сроками выполнения.'
    # else:
        # sel.config(text="Статус не выбран!")
    # def match(y, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя"!#$%&\"/*+/=?^`{|}~" "\\')):
        # return not alphabet.isdisjoint(y.lower())
    # if x != 9:
        # messagebox.showinfo("Ошибка ввода", "Введите корректный номер заявки!")
        # return
    # elif s.isnumeric() == False:
        # messagebox.showinfo("Ошибка ввода", "В номере заявки должны присутвовать только цифры")
        # return
    # elif match(y) == True:
        # messagebox.showinfo("Ошибка ввода", "В адресе присутствуют некорректные символы!")
        # return
    # elif "@" not in y:
        # messagebox.showinfo("Ошибка ввода", "Введите корректный адрес!")
        # return
    # elif '.ru' not in y:
        # messagebox.showinfo("Ошибка ввода", "Введите корректный адрес!")
        # return
    body_text = ""
    isp = 'Исполнителя'
    y = str(surname_entry.get())
    s = str(name_entry.get())
    x = len(s)
    if stat.get() == 1:
        es_type = 'срочности проведения работ.'
        es_work = 'провести работы по заявке БП Инцидент в первую очередь.'
    elif stat.get() == 2:
        es_type = 'непонятном статусе заявки.'
        es_work = 'предоставить заказчику информацию о текущем статусе по заявке в БП Инцидент со сроками выполнения.'
    else:
        sel.config(text="Статус не выбран!", foreground="red")
    def match(y, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя"!#$%&\"/*+/=?^`{|}~" "\\')):
        return not alphabet.isdisjoint(y.lower())
    if x != 9:
        messagebox.showinfo("Ошибка ввода", "Введите корректный номер заявки!")
        return
    elif s.isnumeric() == False:
        messagebox.showinfo("Ошибка ввода", "В номере заявки должны присутвовать только цифры")
        return
    elif match(y) == True:
        messagebox.showinfo("Ошибка ввода", "В адресе присутствуют некорректные символы!")
        return
    elif "@" not in y:
        messagebox.showinfo("Ошибка ввода", "Введите корректный адрес!")
        return  
    body_text = body_text + 'Добрый день!\nПо заявке в БП Инцидент №' + name_entry.get() + ' от заказчика поступила эскалация о ' + es_type
    body_text = body_text + '\nОбращаем внимание ' + isp + ' о необходимости ' + es_work
    # body_text = body_text + '<br><br><i><font size=3><font color="red">Отвечать на данное письмо не требуется</font></i>'
    body_text = body_text + ""
    pyperclip.copy(body_text)
    messagebox.showinfo("Эскалация", body_text)
    return
    
def send_mail():
    root.update()
    outlook = win32.Dispatch('Outlook.Application')
    body_text = ""
    isp = 'Исполнителя'
    y = str(surname_entry.get())
    s = str(name_entry.get())
    x = len(s)
    if stat.get() == 1:
        es_type = 'срочности проведения работ.'
        es_work = 'провести работы по заявке БП Инцидент в первую очередь.'
    elif stat.get() == 2:
        es_type = 'непонятном статусе заявки.'
        es_work = 'предоставить заказчику информацию о текущем статусе по заявке в БП Инцидент со сроками выполнения.'
    else:
        sel.config(text="Статус не выбран!", foreground="red")
    def match(y, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя"!#$%&\"/*+/=?^`{|}~" "\\')):
        return not alphabet.isdisjoint(y.lower())
    if x != 9:
        messagebox.showinfo("Ошибка ввода", "Введите корректный номер заявки!")
        return
    elif s.isnumeric() == False:
        messagebox.showinfo("Ошибка ввода", "В номере заявки должны присутвовать только цифры")
        return
    elif match(y) == True:
        messagebox.showinfo("Ошибка ввода", "В адресе присутствуют некорректные символы!")
        return
    elif "@" not in y:
        mentry.get()
        return
    # elif '.ru' not in y:
    #     messagebox.showinfo("Ошибка ввода", "Введите корректный адрес!")
    #     return
    cc_adress = ''
    mai = []
    mak = []
    
    count = -1
    for i in range (len(mai)): 
        if mai[i] == surname_entry.get(): 
            count = i        
    if count >=0:
        isp = 'группу исполнителей'
        cc_adress = cc_adress + ';' + mak[count] + ''
    body_text = body_text + 'Добрый день!<br><br>По заявке в БП Инцидент №' + name_entry.get() + ' от заказчика поступила эскалация, о ' + es_type
    body_text = body_text + '<br>Обращаем внимание ' + isp + ' о необходимости ' + es_work
    body_text = body_text + '<br><br><i><font size=3><font color="red">Отвечать на данное письмо не требуется</font></i>'
    body_text = body_text + ""
    mail_item = outlook.CreateItem(0) # 0: olMailItem
    mail_item.Recipients.Add(surname_entry.get())
    mail_item.CC = cc_adress
    mail_item.Subject = 'Эскалация от заказчика по заявке в БП Инцидент о срочности/уточнении статуса'
    mail_item.BodyFormat = 2          # 2: Html format
    mail_item.HTMLBody  = body_text
    mail_item.Send()
    logger.info ('124r5')
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    while progress_bar['value'] < 100:
        progress_bar['value'] += 25
        root.update()
        time.sleep(0.5) 
    result.config(text="Письмо отправлено!", font=("Pagella", 10, 'bold'), foreground="green", bg=colorl )
    result.after(5000, lambda: result.config(text=""))
    time.sleep(1)
    progress_bar['value'] = 0
    root.update() 
    
    
#Контекстноке меню начато
class AddPopupMenu:
    def copy_selection(self):
        try:
            selection_text = self.selection_get()
        except tk.TclError:
            return
        root.clipboard_clear()
        root.clipboard_append(selection_text)
        print('Copied:', selection_text)
    def delete_selection(self):
        try:
            self.delete('sel.first', 'sel.last')
        except tk.TclError:
            pass

    def cut_selection(self):
        self.copy_selection()
        self.delete_selection()

    def paste_from_clipboard(self):
        try:
            clipboard_text = root.clipboard_get()
        except tk.TclError:
            pass
        else:
            self.delete_selection()
            self.insert(tk.INSERT, clipboard_text)

    def select_all(self):
        self.tag_add(tk.SEL, "1.0", tk.END)
        self.mark_set(tk.INSERT, "1.0")
        self.see(tk.INSERT)

    def show_context_menu(self, event):
        pos_x = self.winfo_rootx() + event.x
        pos_y = self.winfo_rooty() + event.y
        self.popup_menu.tk_popup(pos_x, pos_y)

    def init_menu(self):
        menu = tk.Menu(self, tearoff=False)
        menu.add_command(label="Вырезать", command=self.cut_selection)
        menu.add_command(label="Копировать", command=self.copy_selection)
        menu.add_command(label="Вставить", command=self.paste_from_clipboard)
        menu.add_command(label="Удалить", command=self.delete_selection)
        menu.add_separator()
        menu.add_command(label="Выделить все", command=self.select_all)
        return menu

    def __init__(self, widget_class, *args, **kwargs):
        widget_class.__init__(self, *args, **kwargs)
        self.popup_menu = self.init_menu()
        self.bind("<3>", self.show_context_menu)
class MyText(tk.Text, AddPopupMenu):
    def __init__(self, *args, **kwargs):
        AddPopupMenu.__init__(self, tk.Text, *args, **kwargs)
class Entry(tk.Entry, AddPopupMenu):
    def __init__(self, *args, **kwargs):
        AddPopupMenu.__init__(self, tk.Entry, *args, **kwargs)
#Контекстное меню закончено

root = tk.Tk()
root.title("Эскалация")
root.geometry("450x260")
#root.resizable(width=False, height=False)
root.attributes('-transparentcolor')
#root.overrideredirect(True)
# test = colorl
root['background'] = colorl
mainmenu = Menu(root)
root.config(menu=mainmenu, bg=colorl)
filemenu = Menu(mainmenu, tearoff=0, fg=color2, bg=colorl)
helpmenu = Menu(mainmenu, tearoff=0, fg=color2, bg=colorl)
#Главное меню
filemenu.add_command(label="Экспорт", command=export)
filemenu.add_command(label="Настройка", command=Them)
mainmenu.add_cascade(label="Файл", menu=filemenu)
# В справке
helpmenu.add_command(label="Справка", command=helpi)
helpmenu.add_command(label="Обновление", command=update)
helpmenu.add_separator() 
helpmenu.add_command(label="О программе", command=about)
#Главное меню
mainmenu.add_cascade(label="Справка", menu=helpmenu)

style = ttk.Style()  
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", fg=color2, bg=colorl )
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100, value=0, style='black.Horizontal.TProgressbar')
progress_bar.grid(row=0, column=0, padx=285, pady=5, sticky="w")
root.update()
progress_bar['value'] = 0

name_label = Label(text="Введите номер заявки:", padx=15, pady=10, font=("Pagella", 9, 'bold'), fg=color2, bg=colorl )
surname_label = Label(text="Введите почту исполнителя:", padx=15, pady=10, font=("Pagella", 9, 'bold'), fg=color2, bg=colorl)
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(width=15, relief='solid', fg=color2, bg=color4)
surname_entry = Entry(width=30, relief='solid', fg=color2, bg=color4)

name_entry.grid(row=0,column=0, padx=180, pady=5, sticky="w")
surname_entry.grid(row=1,column=0, padx=200, pady=0, sticky="w")

# вставка начальных данных. Завязать лна listbox с хранением в csv, когда не будет лень
name_entry.insert(0, "Номер заявки")
surname_entry.insert(0, "E-mail")

stats = [("Срочность", 1), ("Статус", 2)]

stat = IntVar()
header = Label(text="Эскалация по:",  padx=120, pady=5, fg=color2, bg=colorl)
header.grid(row=5, column=0, sticky=W)

row = 5
column = 0
for txt, val in stats:
    Radiobutton(text=txt, value=val, variable=stat, padx=10, pady=0, fg=color2, bg=colorl, selectcolor=color3, command=select)\
        .grid(row=row, column=column, padx=5, sticky=W)
    row += 1
sel = Label(padx=30, pady=5, fg=color2, bg=colorl)
sel.grid(row=5, column=0, padx=200, pady=5, sticky="w")
result = Label(padx=30, pady=5, bg=colorl)
result.grid(row=6, column=0, padx=120, pady=5, sticky="w")
loadimage = PhotoImage(file=b0)
loadimage1 = PhotoImage(file=b1)
loadimage2 = PhotoImage(file=b2)
loadimage3 = PhotoImage(file=b3)
loadimage4 = PhotoImage(file=b4)
loadimagecopy =PhotoImage(file='copy.png')
loadimageadd = PhotoImage(file='book.png')

bia_button = Button(root,text="ГТП БИА", image=loadimage, command=bia1, bg=colorl) 
bia_button["border"] = "0" # Обязательно убираем border!!
bia2_button = Button(root,text="ГПП БИА", image=loadimage1, command=bia2, bg=colorl) 
bia2_button["border"] = "0"
bia3_button = Button(root,text="Мониторинг БИА", image=loadimage2, command=bia3, bg=colorl) 
bia3_button["border"] = "0"
clear_button = Button(root,text="Очистить", image=loadimage3, command=clear, bg=colorl) 
clear_button["border"] = "0"
send_mail_button = Button(root,text="Отправить", image=loadimage4, command=send_mail, bg=colorl) 
send_mail_button["border"] = "0"
display_button = Button(root,text="Смотреть", command=display, bg=colorl) 

addrbook_button = Button(root,text="txt", image=loadimageadd, command=addrbook, bg=colorl) 
addrbook_button.grid(row=1, column=0, padx=400, pady=0, sticky="w")
copy_button = Button(root,text="copy", image=loadimagecopy, command=copy, bg=colorl) 
copy_button.grid(row=0, column=0, padx=400, pady=0, sticky="w")
################################################################

display_button.grid(row=8, column=0, padx=150, pady=5, sticky="w")
send_mail_button.grid(row=8, column=0, padx=250, pady=5, sticky="w")
clear_button.grid(row=8, column=0, padx=40, pady=5, sticky="w")
bia_button.grid(row=3, column=0, padx=10, pady=5, sticky="w")
bia2_button.grid(row=3, column=0, padx=130, pady=5, sticky="w")
bia3_button.grid(row=3, column=0, padx=250, pady=5, sticky="w")

root.mainloop()
