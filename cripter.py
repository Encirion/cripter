import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

root = tk.Tk() #root - имя переменной окна 
root.title(" ")
root.geometry("400x450")
root.resizable(False, False)
#Создаем окно, указываем название и размер в пикселях + блокируем изменене размеров окна виджета

root.configure(bg = "black")
#Задаем цвет фона

style = ttk.Style()
style.theme_use("clam")                   #активация темы оформления clam в ttk
style.configure("Custom.TButton",         #Задаем возможность кастомной настройки кнопки 
                background = "yellow",    #Цвет кнопки
                foreground = "black",     #Цвет текста
                font =( "arial", 15),     #Шрифт и его размер
                padding = (2, 15, 2, 15)) #внутренний отступ внутри кнопки 

#например padding=(10, 5, 10, 5) задаёт 10 пикселей слева и справа, 5 — сверху и снизу. 
#В моем случе задается отступ сразу со всех сторон
def choose_file():
    filepath = filedialog.askopenfilename(title = "choose_file")
    if filepath:
        selected_path_label.config(text=f"Выбрано: {filepath}")

def choose_folder():
    folderpath = filedialog.askdirectory(title="choose_folder")
    if folderpath:
        selected_path_label.config(text=f"Выбрано: {folderpath}")

def show_menu(event):
    menu.post(event.x_root, event.y_root)

label2 = tk.Label(root, 
                 text = "File encryptor using\nthe AES 256 algorithm",
                 bg = "black",fg = "white",
                 font = ("arial", 18)
                 )
label2.pack(anchor = "n",
            padx = 10, pady=20)

button = ttk.Button(root, 
                    text = "нажмите для выбора объекта шифрования",
                    style = "Custom.TButton")
button.pack(pady = 60)   
button.bind("<Button-1>", show_menu)

menu = tk.Menu(root, tearoff=0)
menu.add_command(label = "Выбрать файл", command = choose_file)
menu.add_command(label = "Выбрать папку", command = choose_folder)

selected_path_label = tk.Label(root, 
                 text = "",
                 bg = "black",fg = "white",
                 font = ("arial", 12)
                 )
selected_path_label.pack(anchor="n",
            padx=10, pady=10)

label = tk.Label(root, 
                 text = "make Stanislav",
                 bg = "black",fg = "white",
                 font = ("arial", 14)
                 )
label.pack(anchor = "n",
            padx = 10, pady = 10)
#anchor — якорь, указывает направление:
# 'n' — сверху по центру 
# 'ne' - справа сверху 
# 'nw' - сверху слева 
# 'center' — по центру
# 's', 'se', 'sw' — снизу, спарва и лева соостветственно 
# padx, pady — отступы по оси x и оси y



root.mainloop() 