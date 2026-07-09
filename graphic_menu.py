from tkinter import *
import random
from tkinter import colorchooser
from config import COL3, MAIN_BLUE, CLR, COL_WH, ORNG_2, ORNG, HED_2, HED_2_BOLD, HED_2_ITAL, HED_2_UNDL, SHM_F_L, SHM_F_N, SHM_F_B



def dismiss(window):
    window.grab_release()
    window.destroy()


# Рисунок пингвина из меню Графика
def open_wndw7():
    # Закрытие и открытие глаз
    def motion(event=None):
        def move_down():
            coords = canv.coords(rect)
            current_y2 = coords[3] 
            if current_y2 < 88:
                canv.coords(rect, 98, 50, 155, current_y2 + 5)  # пкс
                wndw7.after(7, move_down)  # мс
            else:
                wndw7.after(700, move_up)

        def move_up():
            coords = canv.coords(rect)
            current_y2 = coords[3]
            if current_y2 > 50:
                canv.coords(rect, 98, 50, 155, current_y2 - 5)
                wndw7.after(7, move_up)

        move_down()

    wndw7 = Toplevel()
    wndw7.title('Пингвин Tux')
    wndw7.configure(bg=COL_WH)
    wndw7.geometry('720x720')
    wndw7.grab_set()


    canv = Canvas(wndw7, width=680, height=620, highlightthickness=FALSE, bg=COL_WH)
    canv.grid(row=0, column=0, sticky='we', padx=10)

    # Черное туловище
    canv.create_polygon([95, 31], [130, 13], [166, 31], [174, 62], [176, 102], 
                        [190, 132], [214, 168], [226, 196], [227, 222], [197, 270], 
                        [156, 290], [128, 290], [100, 288], [62, 260], [42, 214], 
                        [46, 186], [60, 158], [76, 132], [92, 104], [90, 66], outline='white', smooth=1, fill='black')

    # Белый живот
    canv.create_polygon([100, 100], [114, 112], [130, 110], [152, 91], [173, 150], 
                        [188, 192], [180, 202], [168, 206], [160, 256], [140, 264], 
                        [112, 266], [96, 258], [86, 244], [98, 242], [100, 236], 
                        [80, 212], [68, 200], outline='white', smooth=1, fill='white')

    # Глаза
    canv.create_oval([98, 55], [116, 92], fill='white', outline='white')
    canv.create_oval([128, 53], [155, 88], fill='white', outline='white')
    canv.create_oval([102, 64], [111, 84], fill='black', outline='black')
    canv.create_oval([134, 63], [146, 84], fill='black', outline='black')
    rect = canv.create_rectangle([98, 50], [155, 50], fill='black', outline='black')

    # Клюв
    canv.create_polygon([114, 117], [130, 115], [152, 105], [158, 93], [150, 85],
                        [126, 75], [116, 75], [92, 95], [98, 105], outline=ORNG, smooth=1, fill=ORNG_2)
    canv.create_arc([102, 88], [144, 105], start=180, extent=180, style='arc', outline=ORNG, width=2)

    # Лапы
    canv.create_polygon([8, 275], [19, 253], [12, 229], [34, 230], [40, 219], 
                        [58, 207], [90, 248], [96, 256], [105, 285], [94, 298], 
                        [76, 300], [40, 286], [38, 288], outline=ORNG, smooth=1, fill=ORNG_2)

    canv.create_polygon([246, 261], [218, 277], [198, 298], [178, 303], [164, 295], 
                        [156, 283], [160, 261], [164, 221], [169, 207], [179, 225], 
                        [198, 222], [208, 212], [220, 215], [225, 239], outline=ORNG, smooth=1, fill=ORNG_2)

    with open('ABOUT_TUX.txt', 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Текстовое поле справа от рисунка
    txt = Text(canv, height=37, width=44, wrap='word', relief='flat', bg=COL_WH)

    txt.insert('1.0', text_content)
    text_id = canv.create_window(310, 12, anchor='nw', window=txt)

    scr = Scrollbar(wndw7, command=txt.yview)
    
    scr.grid(row=0, column=1, sticky='ns')
    txt.config(yscrollcommand=scr.set)


    # Оформление текста
    txt.tag_add('h1', '1.0', '1.end')
    txt.tag_add('h2', '2.0', END)
    txt.tag_add('cyrsiv', '15.0', END)
    txt.tag_add('underline', '7.0', '7.end')
    txt.tag_add('bgr', '4.17', '4.34')

    txt.tag_config('h1', foreground='black', font=HED_2_BOLD, justify='left')
    txt.tag_config('h2', foreground='black', font=HED_2, justify='left')
    txt.tag_config('cyrsiv', foreground='black', font=HED_2_ITAL, justify='left')
    txt.tag_config('underline', foreground='black', font=HED_2_UNDL, justify='left')
    txt.tag_config('bgr', foreground='black', background=CLR, font=HED_2, justify='left')


    btn_live = Button(wndw7, text='Нажми меня!', command=motion, width=12, bg=CLR)
    btn_live.grid(row=1, column=0, pady=30, sticky='se', padx=10)

    inf = Label(wndw7, text='Нажмите на кнопку (или на пробел, когда окно в фокусе).', 
                font=HED_2_ITAL, fg='black', bg=COL_WH)
    inf.grid(row=1, column=0, padx=20, pady=30, sticky='sw')

    wndw7.bind('<space>', motion)
    wndw7.protocol('WM_DELETE_WINDOW', lambda: dismiss(wndw7))



# Схема из меню Графика
def open_wndw6():
    wndw6 = Toplevel()
    wndw6.title('Схема шифрования изображений с использованием "фильтров-окон" (Filter Windows)')
    wndw6.geometry('1000x780')
    wndw6.grab_set()
    canv = Canvas(wndw6, width=800, height=780)
    canv.pack()
    x = 150
    # Самый большой красный прямоугольник
    canv.create_rectangle(x, 50, x + 350, 180, fill='red', outline='black')

    a = ['red', 'green', 'blue', 'yellow', 'orange', 'violet', 'pink']

    while x < 400:
        color = random.choice(a)
        canv.create_rectangle(x, 50, x + 50, 85, fill='yellowgreen', outline='black', activefill=color)
        x = x + 50
    x = 150
    while x < 400:
        color = random.choice(a)
        canv.create_rectangle(x, 85, x + 50, 120, fill='yellowgreen', outline='black', activefill=color)
        x = x + 50
    x = 150
    while x < 400:
        color = random.choice(a)
        canv.create_rectangle(x, 120, x + 50, 155, fill='yellowgreen', outline='black', activefill=color)
        x = x + 50


    canv.create_text(530, 90, text='Recursively\nEncrypted', font=SHM_F_B, anchor='w', justify='left', fill='black')
    canv.create_text(220, 220, text='Encrypted\nPart', font=SHM_F_B, anchor='w', justify='left', fill='black')
    canv.create_text(120, 260, text='Fig 1(a) Image Encryption using Filter Windows', font=SHM_F_B, anchor='w', justify='left', fill='black')

    # Первый голубой прямоугольник
    canv.create_rectangle(103, 330, 240, 500, fill='lightblue', outline='black')
    x = 140
    while x < 301:
        color = random.choice(a)
        canv.create_rectangle(x, 390, x + 40, 430, fill='yellowgreen', outline='black', activefill=color)
        x = x + 40
    canv.create_rectangle(340, 390, 365, 430, fill='red', outline='black')

    # Второй голубой прямоугольник
    canv.create_rectangle(560, 335, 710, 500, fill='lightblue', outline='black')
    y = 400
    while y < 600:
        color = random.choice(a)
        canv.create_rectangle(610, y, 645, y + 40, fill='yellowgreen', outline='black', activefill=color)
        y = y + 40
    canv.create_rectangle(610, 600, 645, 625, fill='red', outline='black')

    canv.create_text(575, 685, text='Recursively\nEncrypted\nPart', font=SHM_F_N, anchor='w', justify='left', fill='black')

    canv.create_text(20, 390, text='UNUSED\nFILTER', font=SHM_F_L, anchor='w', justify='left', fill='black')
    canv.create_text(20, 465, text='FILTER', font=SHM_F_L, anchor='w', justify='left', fill='black')
    canv.create_text(530, 540, text='IMAGE', font=SHM_F_L, anchor='w', justify='left', fill='black')

    canv.create_text(668, 297, text='UNUSED\nFILTER', font=SHM_F_L, anchor='w', justify='left', fill='black')
    canv.create_text(585, 300, text='FILTER', font=SHM_F_L, anchor='w', justify='left', fill='black')
    canv.create_line(591, 307, 591, 335, width=1, fill='black', arrow='first')

    # вертикальная стрелка
    canv.create_line(674, 314, 674, 352, width=12, fill='black', arrow='first')
    canv.create_line(674, 315, 674, 351, width=10, fill='lightblue', arrow='first')

    canv.create_line(275, 149, 275, 195, width=12, fill='black', arrow='last')
    canv.create_line(275, 150, 275, 194, width=10, fill='lightblue', arrow='last')

    canv.create_text(385, 410, text='Recursively Encrypted\nPart', font=SHM_F_L, anchor='w', justify='left', fill='black')
    canv.create_text(260, 475, text='IMAGE', font=SHM_F_L, anchor='w', justify='left', fill='black')

    canv.create_line(280, 430, 280, 460, width=1, fill='black', arrow='last')
    canv.create_line(580, 540, 610, 540, width=1, fill='black', arrow='first')

    canv.create_line(627, 613, 627, 649, width=12, fill='black', arrow='last')
    canv.create_line(627, 614, 627, 648, width=10, fill='lightblue', arrow='last')

    canv.create_line(70, 465, 103, 465, width=1, fill='black', arrow='first')

    canv.create_line(350, 415, 379, 415, width=12, fill='black', arrow='last')
    canv.create_line(351, 415, 378, 415, width=10, fill='lightblue', arrow='last')

    # вертикальная стрелка
    canv.create_line(310, 360, 310, 401, width=12, fill='black', arrow='first')
    canv.create_line(310, 361, 310, 400, width=10, fill='lightblue', arrow='first')
    canv.create_text(255, 340, text='Encrypted Part', font=SHM_F_L, anchor='w', justify='left', fill='black')

    canv.create_line(480, 73, 521, 73, width=12, fill='black', arrow='last')
    canv.create_line(481, 73, 520, 73, width=10, fill='lightblue', arrow='last')

    canv.create_line(638, 570, 668, 570, width=12, fill='black', arrow='last')
    canv.create_line(639, 570, 667, 570, width=10, fill='lightblue', arrow='last')
    canv.create_text(683, 570, text='Encrypted Part', font=SHM_F_L, anchor='w', justify='left', fill='black')

    canv.create_line(78, 390, 111, 390, width=12, fill='black', arrow='first')
    canv.create_line(79, 390, 110, 390, width=10, fill='lightblue', arrow='first')
    wndw6.protocol('WM_DELETE_WINDOW', lambda: dismiss(wndw6))



# Окно движущегося квадрата (Меню Графика)
def open_wndw8():
    wndw8 = Toplevel()
    wndw8.title('Анимация')
    wndw8.geometry('400x300')
    wndw8.grab_set()
    canvas = Canvas(wndw8, width=400, height=300, bg="white")
    canvas.pack()

    x, y = 50, 50
    dx, dy = 3, 2
    size = 20

    def animate():
        if not wndw8.winfo_exists():
            return
        nonlocal x, y, dx, dy
        canvas.delete("shape")
        x += dx
        y += dy

        if x + size > 400 or x < 0:
            dx = -dx
            x = max(0, min(400 - size, x))
        if y + size > 300 or y < 0:
            dy = -dy
            y = max(0, min(300 - size, y))

        canvas.create_rectangle(x, y, x + size, y + size, fill=MAIN_BLUE, tags="shape")
        wndw8.after(10, animate)
    animate()
    wndw8.protocol('WM_DELETE_WINDOW', lambda: dismiss(wndw8))



    # Окно палитры выбора цвета из меню Графика
def open_wndw3():
    def chose_color():
        color = colorchooser.askcolor()
        if color[1] != None:
            color_label.config(bg=color[1])

    wndw3 = Toplevel()
    wndw3.title('Палитра цветов')
    wndw3.geometry('400x200')
    wndw3.grab_set()

    btn = Button(wndw3, text='Выбрать цвет', command=chose_color, bg=COL3, width=13)
    btn.pack(side=LEFT, padx=30, pady=30)

    color_label = Label(wndw3, width=15, height=7, bg='dark cyan', relief='sunken')
    color_label.pack(side=LEFT, padx=10)

    wndw3.protocol('WM_DELETE_WINDOW', lambda: dismiss(wndw3))



# Цветной фрейм из меню Графика
def open_wndw2():
    wndw2 = Toplevel()
    wndw2.title('Изменение размера рамки')
    wndw2.geometry('500x370')
    wndw2.grab_set()

    fra1 = Frame(wndw2, width=500, height=100, bg=COL3)
    fra1.pack()
    fra1.pack_propagate(False)

    def change_color(value_s):
        val = int(value_s)
        r = val
        g = 0
        b = 255
        color = f'#{r:02x}{g:02x}{b:02x}'
        fra1.config(bg=color)

    cur_val = IntVar()
    scale1 = Scale(fra1, from_=0, to=255, orient='horizontal', length=300, tickinterval=50, variable=cur_val, command=change_color)
    scale1.pack(padx=20, pady=20)
    wndw2.protocol('WM_DELETE_WINDOW', lambda: dismiss(wndw2))

    def size3():
        fra1.config(width=500, height=150)
    def size4():
        fra1.config(width=500, height=200)
    def size5():
        fra1.config(width=500, height=250)    

    btn15 = Button(wndw2, command=size3, text='Размер фрейма: 500х150', bg=COL3)
    btn20 = Button(wndw2, command=size4, text='Размер фрейма: 500х200', bg=COL3)
    btn25 = Button(wndw2, command=size5, text='Размер фрейма: 500х250', bg=COL3)
    btn15.pack(anchor='center', pady=5)
    btn20.pack(anchor='center', pady=5)
    btn25.pack(anchor='center', pady=5)