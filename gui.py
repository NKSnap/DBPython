from tkinter import *
from tkinter import messagebox as mess
from strings import *
from DBClass import DBClass
import DBHelper
import sys


# READY
def exit_click():
    DBHelper.write()
    sys.exit()


# READY
def add_click():
    entrys = list()

    def click():
        variables = list()
        for i in entrys:
            variables.append(i.get())

        for i in variables:
            if i == '':
                mess.showinfo(ERROR, FIELDS_ERROR)
                add_activity.destroy()
                return

        DBHelper.NOTE_LIST.append(DBClass(str(len(DBHelper.NOTE_LIST) + 1), variables[1], variables[2],
                                          variables[3], variables[0], variables[4], variables[5],
                                          variables[6], variables[7]))
        mess.showinfo("ДОБАВЛЕНИЕ", "Новый элемент добавлен!")
        DBHelper.write()
        add_activity.destroy()

    def add_UI():
        r = -2
        for i in range(len(ADD_INFO)):
            r += 2
            Label(add_activity, text=ADD_INFO[i], font=('Arial', 10)).grid(row=r, column=0, pady=5, padx=10, sticky=W)
            entrys.append(Entry(add_activity, width=50, bd=3, justify=LEFT))
            entrys[i].grid(row=r + 1, column=0)

        Button(add_activity, text="Добавить", width=30, bd=5, padx=45, pady=5,
               command=click).grid(row=r + 2, column=0)

    add_activity = Tk()
    add_activity.title("Добавление")
    add_activity.resizable(False, False)
    add_UI()
    add_activity.mainloop()


# READY
def delete_click():
    def click():
        if entry_id.get() != '':
            try:
                delete_ID = int(entry_id.get())
                DBHelper.NOTE_LIST.pop(delete_ID - 1)
                DBHelper.write()
                mess.showinfo("УДАЛЕНИЕ", "Элемент был удалён!")
            except Exception:
                mess.showinfo(ERROR, ID_ERROR)
            delete_activity.destroy()

    delete_activity = Tk()
    delete_activity.title("Удаление")
    delete_activity.resizable(False, False)

    Label(delete_activity, text=DELETE_INFO, justify=LEFT) \
        .pack(anchor="nw", padx=10, pady=5)

    entry_id = Entry(delete_activity, width=50, bd=3, justify=LEFT)
    entry_id.pack(padx=5)

    Button(delete_activity, text="Удалить", width=43, bd=5,
           command=click).pack()


# READY
def show_click():
    entrys = list()

    def edit_click():
        check_element = listbox.curselection()

        def click_on_edit():
            if len(check_element) != 1:
                mess.showinfo(ERROR, SELECTION_ERROR)
                return
            try:
                edit_node = DBHelper.NOTE_LIST[check_element[0]].get_list()
                variables = [check_element[0] + 1]
                for k in entrys:
                    variables.append(k.get())

                for n in range(len(variables)):
                    if variables[n] != '':
                        edit_node[n] = variables[n]

                o = DBClass(edit_node[0],
                            edit_node[1], edit_node[2], edit_node[3], edit_node[4], edit_node[5],
                            edit_node[6], edit_node[7], edit_node[8])
                DBHelper.NOTE_LIST[check_element[0]] = o
                DBHelper.write()
                mess.showinfo("РЕДАКТИРОВАНИЕ", "Элемент изменён!")
                edit_activity.destroy()
                show_activity.destroy()
                return
            except Exception:
                mess.showinfo(ERROR, UNKNOWN_ERROR)

        def add_UI():
            r = -2
            for k in range(len(SHOW_INFO)):
                r += 2
                Label(edit_activity, text=SHOW_INFO[k]).grid(row=r, column=0, pady=5)
                entrys.append(Entry(edit_activity, width=50, bd=3, justify=LEFT))
                entrys[k].grid(row=r + 1, column=0)

            Button(edit_activity, text="Добавить", width=30, bd=5, padx=45, pady=5,
                   command=click_on_edit).grid(row=r + 2, column=0)

        edit_activity = Tk()
        edit_activity.title("Редактирование")
        edit_activity.resizable(False, False)
        add_UI()
        edit_activity.mainloop()

    def click_on_show(event):
        element = listbox.curselection()
        if len(element) == 1:
            try:
                params = DBHelper.NOTE_LIST[element[0]].get_full_string().replace('  ', '').split('|')
                res_text = SHOW_FORMAT % (params[2], params[3], params[4],
                                          params[5], params[6], params[7], params[9], params[8])
                inf_activity = Tk()
                inf_activity.title("Информация")
                inf_activity.resizable(False, False)

                edit_menu = Menu(inf_activity)
                edit_menu.add_cascade(label="Редактировать", command=edit_click)
                inf_activity.config(menu=edit_menu)

                Label(inf_activity, justify=LEFT, text=res_text, font=('Arial', 12)) \
                    .pack(anchor="nw")
                inf_activity.mainloop()
            except Exception:
                mess.showinfo(ERROR, VALUE_ERROR)

    show_activity = Tk()
    show_activity.title("Список")
    show_activity.geometry("420x480")
    show_activity.resizable(False, False)

    scrollbarY = Scrollbar(show_activity)
    scrollbarY.pack(side=RIGHT, fill=Y)

    listbox = Listbox(show_activity, width=100, height=40, yscrollcommand=scrollbarY.set, font=14)
    scrollbarY.config(command=listbox.yview)
    listbox.bind('<Button-2>', click_on_show)

    length = len(DBHelper.NOTE_LIST)
    for i in range(length):
        listbox.insert(END, DBHelper.NOTE_LIST[i].show_string())

    listbox.pack()
    show_activity.mainloop()


# READY
def order_click():
    entrys = list()

    def show(num):
        try:
            params = DBHelper.NOTE_LIST[num].get_full_string().replace('  ', '').split('|')
            res_text = SHOW_FORMAT % (params[2], params[3], params[4],
                                      params[5], params[6], params[7], params[9], params[8])
            inf_activity = Tk()
            inf_activity.title("Информация")
            inf_activity.resizable(False, False)

            Label(inf_activity, justify=LEFT, text=res_text, font=('Arial', 10)).pack()
            inf_activity.mainloop()
        except Exception:
            mess.showinfo(ERROR, VALUE_ERROR)

    def order(nodes):
        def click(event):
            element = listbox.curselection()
            if len(element) == 1:
                show(num=element[0])

        order_activity.destroy()
        show_order_activity = Tk()
        show_order_activity.title("Отфильтрованный список")
        show_order_activity.geometry("420x480")
        show_order_activity.resizable(False, False)

        scrollbarY = Scrollbar(show_order_activity)
        scrollbarY.pack(side=RIGHT, fill=Y)

        listbox = Listbox(show_order_activity, width=100, height=40, yscrollcommand=scrollbarY.set, font=14)
        scrollbarY.config(command=listbox.yview)
        listbox.bind('<Button-2>', click)

        for i in range(len(nodes)):
            listbox.insert(END, nodes[i].show_string())

        listbox.pack()
        show_order_activity.mainloop()

    def order_by_version():
        version = entrys[0].get()
        if version == '':
            mess.showinfo(ERROR, VERSION_ERROR)
            order_activity.destroy()
            return

        for o in DBHelper.NOTE_LIST:
            if o.get_list()[1] == version:
                order_list.append(o)
        order(nodes=order_list)

    def order_by_name():
        name = entrys[1].get()
        if name == '':
            mess.showinfo(ERROR, NAME_ERROR)
            order_activity.destroy()
            return

        for o in DBHelper.NOTE_LIST:
            if o.get_list()[4] == name:
                order_list.append(o)
        order(nodes=order_list)

    def order_by_price():
        price1 = entrys[2].get()
        price2 = entrys[3].get()
        if price1 == '' and price2 == '':
            mess.showinfo(ERROR, RANGE_ERROR)
            order_activity.destroy()
            return
        elif price1 == '':
            for o in DBHelper.NOTE_LIST:
                parameters = o.get_list()
                if parameters[5] == price2:
                    order_list.append(o)
        elif price2 == '':
            for o in DBHelper.NOTE_LIST:
                parameters = o.get_list()
                if parameters[5] == price1:
                    order_list.append(o)
        else:
            try:
                for o in DBHelper.NOTE_LIST:
                    parameters = o.get_list()
                    if int(price1) <= int(parameters[5]) <= int(price2):
                        order_list.append(o)
            except Exception:
                mess.showinfo(ERROR, TYPES_ERROR)
                order_activity.destroy()
                return
        order(nodes=order_list)

    def order_UI():
        r = -4
        n = -2
        for i in range(3):
            r += 4
            n += 2
            Label(order_activity, text=ORDER_INFO[n], font=('Arial', 12)) \
                .grid(row=r, column=0, pady=5)
            Label(order_activity, text=ORDER_INFO[n + 1], font=('Arial', 10), justify=LEFT) \
                .grid(row=r + 1, column=0, sticky=W, padx=10)

            entrys.append(Entry(order_activity, width=50, bd=3, justify=LEFT))
            entrys[i].grid(row=r + 2, column=0, pady=3)

            if i == 0:
                Button(order_activity, text="Показать", width=42, bd=5, command=order_by_version) \
                    .grid(row=r + 3, column=0)
            elif i == 1:
                Button(order_activity, text="Показать", width=42, bd=5, command=order_by_name) \
                    .grid(row=r + 3, column=0)
            else:
                entrys.append(Entry(order_activity, width=50, bd=3, justify=LEFT))
                entrys[i + 1].grid(row=r + 3, column=0, pady=3)
                Button(order_activity, text="Показать", width=42, bd=5, command=order_by_price) \
                    .grid(row=r + 4, column=0)

    order_list = list()
    order_activity = Tk()
    order_activity.title("Фильтрация")
    order_activity.resizable(False, False)
    order_UI()
    order_activity.mainloop()


# READY
def main_gui():
    def labels():
        Label(main_activity, text=INFO, font=("Arial", 16), bg=BACKGROUND).pack()

        Label(main_activity, text=INFO_DEVELOPER,
              font=("Arial", 13, "italic"), bg=BACKGROUND).pack()

        Label(main_activity, text=APP_HELP, font=("Arial", 14, "bold"), bg=BACKGROUND) \
            .pack(anchor="nw", padx=50, pady=30)

        for i in range(6):
            Label(main_activity, text=MAIN_ITEMS[i], font=("Arial", 13), justify=LEFT) \
                .pack(anchor="nw", padx=50, pady=5)

    DBHelper.read()
    main_activity = Tk()
    main_activity.title("Приложение")
    main_activity.geometry("1080x560")
    main_activity["bg"] = BACKGROUND
    labels()

    main_menu = Menu()
    options_menu = Menu()
    options_menu.add_command(label="Добавить", command=add_click)
    options_menu.add_command(label="Удалить", command=delete_click)
    options_menu.add_command(label="Показать", command=show_click)
    main_menu.add_cascade(label="Опции", menu=options_menu)
    main_menu.add_cascade(label="Редактировать", command=show_click)
    main_menu.add_cascade(label="Отфильтровать", command=order_click)
    main_menu.add_cascade(label="Выйти", command=exit_click)

    main_activity.config(menu=main_menu)
    main_activity.mainloop()


main_gui()
