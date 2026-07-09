from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from config import COL3, COL_WH, MAIN_BLUE, HED_3_BOLD, BIG_FONT, HED_2


# Окно из меню Инструменты
def open_wndw4():
    primer = ''
    wndw4 = Toplevel()
    wndw4.resizable(False, False)
    wndw4.title('Калькулятор')
    wndw4.geometry('245x360')
    input_text = StringVar()

    def press(item):
        nonlocal primer
        primer = primer + str(item)
        input_text.set(primer)
    
    def clear():
        nonlocal primer
        primer = ''
        input_text.set('')
    
    def ravno():
        nonlocal primer
        try:
            expression = primer.replace(',', '.')
            result_fl = eval(expression)
            if isinstance(result_fl, float) and result_fl.is_integer():
                result_str = str(int(result_fl))
            else:
                result_str = "{:.4f}".format(result_fl).rstrip('0').rstrip('.') if isinstance(result_fl, float) else str(result_fl)
            input_text.set(result_str)
            primer = result_str
        except:
            input_text.set('Ошибка!')
            primer = ''

    dis = Label(wndw4, textvariable=input_text, font=BIG_FONT, bg=COL_WH, 
                   anchor='e', width=15, bd=5, relief='sunken')
    dis.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

    clear_btn = Button(wndw4, text='Стереть', width=14, height=2, command=clear, bg=COL3, font=HED_3_BOLD)
    clear_btn.grid(row=1, column=0, columnspan=2)
    ravno_btn = Button(wndw4, text='=', width=14, height=2, command=ravno, bg=COL3, font=HED_3_BOLD)
    ravno_btn.grid(row=1, column=2, columnspan=2)
    
    Button(wndw4, text='7', width=7, height=2, command=lambda: press(7)).grid(row=2, column=0)
    Button(wndw4, text='8', width=7, height=2, command=lambda: press(8)).grid(row=2, column=1)
    Button(wndw4, text='9', width=7, height=2, command=lambda: press(9)).grid(row=2, column=2)
    Button(wndw4, text='/', width=7, height=2, command=lambda: press('/')).grid(row=2, column=3)
    Button(wndw4, text='4', width=7, height=2, command=lambda: press(4)).grid(row=3, column=0)
    Button(wndw4, text='5', width=7, height=2, command=lambda: press(5)).grid(row=3, column=1)
    Button(wndw4, text='6', width=7, height=2, command=lambda: press(6)).grid(row=3, column=2)
    Button(wndw4, text='*', width=7, height=2, command=lambda: press('*')).grid(row=3, column=3)
    Button(wndw4, text='1', width=7, height=2, command=lambda: press(1)).grid(row=4, column=0)
    Button(wndw4, text='2', width=7, height=2, command=lambda: press(2)).grid(row=4, column=1)
    Button(wndw4, text='3', width=7, height=2, command=lambda: press(3)).grid(row=4, column=2)
    Button(wndw4, text='-', width=7, height=2, command=lambda: press('-')).grid(row=4, column=3)
    Button(wndw4, text='0', width=7, height=2, command=lambda: press(0)).grid(row=5, column=0)
    Button(wndw4, text='.', width=7, height=2, command=lambda: press('.')).grid(row=5, column=1)
    Button(wndw4, text='+', width=7, height=2, command=lambda: press('+')).grid(row=5, column=2)



# Окно текстового редактора (Меню Инструменты)
def open_txt_editor():
    # Переменная для хранения пути к текущему файлу
    current_file = None

    def update_title():
        if current_file:
            wndw9.title(f'Текстовый редактор - {current_file}')
        else:
            wndw9.title('Текстовый редактор - Новый файл')

    def _new_file():
        nonlocal current_file
        if askyesno("Новый файл", "Очистить текущий текст? Несохраненные данные будут потеряны."):
            txt.delete(1.0, END)
            current_file = None
            update_title()

    def _open():
        nonlocal current_file
        op = askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if op: # если пользователь не нажал "Отмена"
            try:
                with open(op, "r", encoding="utf-8") as f:
                    content = f.read()
                    txt.delete(1.0, END)
                    txt.insert(END, content)
                current_file = op
                update_title()
            except Exception as e:
                showerror("Ошибка", f"Не удалось открыть файл: {e}")

    def _save():
        nonlocal current_file
        if current_file: # Если файл уже имеет путь, просто сохраняем
            try:
                letter = txt.get(1.0, END)
                with open(current_file, "w", encoding="utf-8") as f:
                    f.write(letter.rstrip())
            except Exception as e:
                showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        else:
            _save_as()

    def _save_as():
        nonlocal current_file
        sa = asksaveasfilename(defaultextension=".txt", 
                               filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if sa:
            current_file = sa
            _save()
            update_title()

    def close_win():
        if askyesno("Выход", "Выйти из редактора? Убедитесь, что вы сохранили изменения."):
            wndw9.destroy()


    wndw9 = Toplevel()
    wndw9.geometry('600x400')
    wndw9.grab_set()
    update_title()

    m = Menu(wndw9)
    wndw9.config(menu=m)
    
    fm = Menu(m, tearoff=0)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Новый", command=_new_file, 
               activebackground=MAIN_BLUE, activeforeground='black')
    fm.add_command(label="Открыть", command=_open, 
               activebackground=MAIN_BLUE, activeforeground='black')
    fm.add_command(label="Сохранить", command=_save, 
               activebackground=MAIN_BLUE, activeforeground='black')
    fm.add_command(label="Сохранить как...", command=_save_as, 
               activebackground=MAIN_BLUE, activeforeground='black')

  
    frame = Frame(wndw9)
    frame.pack(fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    txt = Text(frame, font=HED_2, undo=True, yscrollcommand=scrollbar.set)
    txt.pack(fill=BOTH, expand=True)
    
    scrollbar.config(command=txt.yview)
    wndw9.protocol('WM_DELETE_WINDOW', close_win)