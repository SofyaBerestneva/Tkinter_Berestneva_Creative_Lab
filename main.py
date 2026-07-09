from tkinter import *
from tkinter.messagebox import *

from tools_menu import open_wndw4, open_txt_editor
from graphic_menu import open_wndw7, open_wndw6, open_wndw8, open_wndw3, open_wndw2
from spravka_menu import open_wndw5
from config import COL_WH, MAIN_BLUE, MAIN_ICON, HED_2, HED_1_ITAL, COL_D, COL_D1


wndw = Tk()
wndw.title('Творческая Лаборатория')
wndw.geometry('650x608')
wndw.configure(bg=COL_WH)

icon_image = PhotoImage(file=MAIN_ICON) 
# все Toplevel окна
wndw.iconphoto(True, icon_image)  

welcome_text = ('Добро пожаловать в Творческую Лабораторию!\n\n'
                'Здесь точность расчетов встречается с полетом фантазии.\n'
                'Данное приложение все еще находится в разработке\nи постоянно улучшается, спасибо за понимание.\n'
                'Используйте меню для доступа к возможностям.')

wel_txt = Text(wndw, width=50, height=6, wrap='word', bg=COL_WH, bd=0)
wel_txt.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky='ew')

wel_txt.insert(1.0, welcome_text)
wel_txt.tag_add('hed1', '1.0', '1.end')
wel_txt.tag_add('hed2', '2.0', END)
wel_txt.tag_config('hed1', foreground='black', font=HED_1_ITAL, justify='center')
wel_txt.tag_config('hed2', foreground='black', font=HED_2, justify='center')

# Настройка сетки для грида
wndw.grid_rowconfigure(0, weight=1)
wndw.grid_rowconfigure(1, weight=0)
wndw.grid_rowconfigure(2, weight=0) 
wndw.grid_columnconfigure(0, weight=1)
wndw.grid_columnconfigure(1, weight=0)


fr1 = Frame(wndw, width=700, height=205, borderwidth=7, relief='ridge', bg=COL_WH)
fr1.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky='ew')
fr1.pack_propagate(False)

# Сетка внутри fr1
fr1.grid_rowconfigure(0, weight=1)
fr1.grid_rowconfigure(1, weight=1)
fr1.grid_rowconfigure(2, weight=1)
fr1.grid_rowconfigure(3, weight=1)
fr1.grid_rowconfigure(4, weight=1)
fr1.grid_columnconfigure(0, weight=1)
fr1.grid_columnconfigure(1, weight=2)
fr1.grid_columnconfigure(2, weight=1)


lbl3 = Label(fr1, text='Выберите значения и кликните\nпо текстовому полю ЛКМ или ПКМ', 
             font=HED_2, bg=COL_WH)
lbl3.grid(row=0, column=0, pady=10, padx=10, sticky='w')

# Группа флажков слева главного окна
answr4 = StringVar(value='-')
answr5 = StringVar(value='-')
answr6 = StringVar(value='-')
chbtn4 = Checkbutton(fr1, text='Цветовая теория', variable=answr4, 
                     onvalue='Цветовая теория', offvalue='-', bg=COL_WH, 
                     font=HED_2, activebackground=COL_WH)
chbtn4.grid(row=1, column=0, padx=10, pady=2, sticky='w')

chbtn5 = Checkbutton(fr1, text='Архитектура композиции', variable=answr5, 
                     onvalue='Архитектура композиции', offvalue='-', bg=COL_WH, 
                     font=HED_2, activebackground=COL_WH)
chbtn5.grid(row=2, column=0, padx=10, pady=2, sticky='w')

chbtn6 = Checkbutton(fr1, text='Технический чертеж', variable=answr6, 
                     onvalue='Технический чертеж', offvalue='-', bg=COL_WH, 
                     font=HED_2, activebackground=COL_WH)
chbtn6.grid(row=3, column=0, padx=10, pady=2, sticky='w')
chbtn4.deselect()
chbtn5.deselect()
chbtn6.deselect()

tex = Text(fr1, width=30, height=2, font=HED_2, wrap='word')
tex.grid(row=4, column=0, padx=10, pady=10, sticky='ew')


def select():   
    """Именение цвета дома независимо от дня или ночи"""
    can1.itemconfigure("house", fill=selected_color.get())

def select_wndw():
    """Изменение цвета окна дома и фона День/Ночь"""
    can1.itemconfigure("window", fill=selected_state.get())
    can1.configure(bg='navy blue')
    if selected_state.get() == on_:
        can1.configure(bg=COL_WH)


# Дом и радиокнопки для отображения названий цветов на окне
blue1 = 'cadet blue'
blue = 'medium slate blue'
green = 'ForestGreen'
on_ = 'light blue'
off_ = 'yellow'

selected_state = StringVar(value=on_)
selected_color = StringVar(value=blue1)

# Холст с домом
can1 = Canvas(fr1, bg="white", width=90, height=130)
can1.grid(row=0, column=1, pady=10, sticky='ew')

can1.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
can1.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")
can1.create_rectangle((70, 90, 90, 115), fill=selected_state.get(), outline="black", tags="window")


ro = Radiobutton(fr1, text='День', value=on_, 
                 variable=selected_state, command=select_wndw, 
                 bg=COL_WH, font=HED_2, activebackground=COL_WH)
ro.grid(row=1, column=1, pady=4, sticky='w')
rf = Radiobutton(fr1, text='Ночь', value=off_, 
                 variable=selected_state, command=select_wndw, 
                 bg=COL_WH, font=HED_2, activebackground=COL_WH)
rf.grid(row=2, column=1, pady=4, sticky='w')

r1 = Radiobutton(fr1, text=blue1, value=blue1,
                  variable=selected_color, command=select, 
                  bg=COL_WH, font=HED_2, activebackground=COL_WH)
r1.grid(row=1, column=2, pady=4, sticky='w')
r2 = Radiobutton(fr1, text=blue, value=blue, 
                 variable=selected_color, command=select, 
                 bg=COL_WH, font=HED_2, activebackground=COL_WH)
r2.grid(row=2, column=2, pady=4, sticky='w')
r3 = Radiobutton(fr1, text=green, value=green, 
                 variable=selected_color, command=select,
                  bg=COL_WH, font=HED_2, activebackground=COL_WH)
r3.grid(row=3, column=2, pady=4, sticky='w')


# Нижняя часть окна с шаром
c = Canvas(wndw, width=810, height=60, bg=COL_WH, highlightbackground=COL_WH)
c.grid(row=2, column=0, columnspan=2, sticky='ew')

dx = 2
ball = c.create_oval(0, 10, 40, 50, fill=MAIN_BLUE)

def motion():
    pos = c.coords(ball)
    x1, y1, x2, y2 = pos
    if x2 >= 650:
        global dx
        dx = -abs(dx)
    elif x1 <= 0:
        dx = abs(dx)
    c.move(ball, dx, 0)
    wndw.after(9, motion)

motion()



# Выбор темы главного окна
def dark_theme():
    fr1.config(background=COL_D)
    wndw.configure(bg=COL_D1)
    wel_txt.config(bg=COL_D1)
    wel_txt.tag_config('hed1', foreground='white')
    wel_txt.tag_config('hed2', foreground='white')

    chbtn4.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    chbtn5.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    chbtn6.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    lbl3.config(bg=COL_D, fg=COL_WH)

    r1.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    r2.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    r3.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    ro.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    rf.config(bg=COL_D, activebackground=COL_D, fg=COL_WH, selectcolor=COL_D)
    c.configure(bg=COL_D1, highlightbackground=COL_D1)

def light_theme():
    fr1.config(bg=COL_WH)
    wndw.configure(bg=COL_WH)
    wel_txt.config(bg=COL_WH)
    wel_txt.tag_config('hed1', foreground='black')
    wel_txt.tag_config('hed2', foreground='black')

    chbtn4.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    chbtn5.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    chbtn6.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    lbl3.config(bg=COL_WH, fg='black')

    r1.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    r2.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    r3.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    ro.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    rf.config(bg=COL_WH, activebackground=COL_WH, fg='black', selectcolor=COL_WH)
    c.configure(bg=COL_WH, highlightbackground=COL_WH)



m = Menu(wndw)
wndw.config(menu=m)

view = Menu(m)
m.add_cascade(label='Вид', menu=view)
view.add_command(label='Светлая тема', command=light_theme, 
                 activebackground=MAIN_BLUE, activeforeground='black')
view.add_command(label='Темная тема', command=dark_theme, 
                 activebackground=MAIN_BLUE, activeforeground='black')

tools = Menu(m)
m.add_cascade(label='Инструменты', menu=tools)
tools.add_command(label='Калькулятор', command=open_wndw4, 
                  activebackground=MAIN_BLUE, activeforeground='black')
tools.add_command(label='Текстовый редактор', command=open_txt_editor, 
                  activebackground=MAIN_BLUE, activeforeground='black')

graphics = Menu(m)
m.add_cascade(label='Графика', menu=graphics)
graphics.add_command(label='Схема шифрования изображений', command=open_wndw6, 
                     activebackground=MAIN_BLUE, activeforeground='black')
graphics.add_command(label='Пингвин Tux', command=open_wndw7,
                     activebackground=MAIN_BLUE, activeforeground='black')
graphics.add_command(label='Анимация', command=open_wndw8, 
                     activebackground=MAIN_BLUE, activeforeground='black')
graphics.add_command(label='Палитра цветов', command=open_wndw3, 
                     activebackground=MAIN_BLUE, activeforeground='black')
graphics.add_command(label='Цвет рамки', command=open_wndw2, 
                     activebackground=MAIN_BLUE, activeforeground='black')

info = Menu(m)
m.add_cascade(label='Справка', menu=info)
info.add_command(label='Интерестные факты об искусстве', command=open_wndw5, 
                 activebackground=MAIN_BLUE, activeforeground='black')

# Показ в текстовом поле по клику ЛКМ выбранных флажков, а по клику ПКМ - не выбранных
def unchosen(event):
    l = []
    val4 = answr4.get()
    val5 = answr5.get()
    val6 = answr6.get()
    if val4 == '-': l.append('Цветовая теория')
    if val5 == '-': l.append('Архитектура композиции')
    if val6 == '-': l.append('Технический чертеж')
    output_unchosen = ', '.join([item for item in l if item != '-'])
    tex.delete(1.0, END)
    tex.insert(END, output_unchosen)
    return 'break'

def chosen(event):
    l1 = []
    val4 = answr4.get()
    val5 = answr5.get()
    val6 = answr6.get()
    if val4 != '-': l1.append(val4)
    if val5 != '-': l1.append(val5)
    if val6 != '-': l1.append(val6)
    output_chosen = ', '.join(l1)
    tex.delete(1.0, END)
    tex.insert(END, output_chosen)
    return 'break'

tex.bind('<Button-1>', chosen)
tex.bind('<Button-3>', unchosen)



def close_win(window):
    if askyesno('Выход', 'Вы уверены, что хотите выйти?'):
        window.destroy()

wndw.protocol('WM_DELETE_WINDOW', lambda: close_win(wndw))

wndw.mainloop()