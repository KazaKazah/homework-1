from tkinter import *

# # Задание 1
# Напишите программу с интерфейсом, которая будет по нажатию кнопки создавать много файлов внутри папки «temp». 
# оличество файлов нужно выбирать через spinbox на интерфейсе.
spinbox_widget = None

def create_many_files():
    global spinbox_widget
    if spinbox_widget is not None:
        with open("spinbox_widget", "w") as file:
            a = file.write("")
            a = spinbox_widget.get()


def create_ui():
    root = Tk()

    root.title("Name")
    root.geometry("300x250")

    btn = Button(root, text="Click", bg="green", command=create_many_files)
    btn.pack()

    sbx = Spinbox(root, width=25, bg="blue", fg="white", from_=1, to=500)
    sbx.pack()
    global spinbox_widget
    spinbox_widget = sbx

    print(sbx.get())

    root.mainloop()


create_ui()

# # Задание 2
# Соберите приложение в одну папку и отдельно в один файл, с помощью «pyinstaller».
