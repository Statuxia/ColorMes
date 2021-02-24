from tkinter import Tk, Text, Label, Button, DISABLED, NORMAL, END
import webbrowser

colormap = {'0': 'black', '1': 'blue', '2': 'green3', '3': 'green4', '4': 'cyan3', '5': 'magenta3', '6': 'orange',
            '7': 'gray65', '8': 'gray35', '9': 'royal blue', 'a': 'lawn green', 'b': 'cyan2', 'c': 'tomato',
            'd': 'orchid2', 'e': 'yellow', 'f': 'white'}

def forum():
    webbrowser.open("https://forum.vimeworld.ru/topic/741824-colormes")

def url():
    webbrowser.open("https://github.com/Statuxia/ColorMes")


def copy():
    Demo.clipboard_clear()
    Demo.clipboard_append(Input.get(1.0, END)[:-1])


def delete():
    Demo.config(state=NORMAL)
    Demo.delete('1.0', END)
    Demo.config(state=DISABLED)
    Input.delete('1.0', END)

def clicked():
    text = Input.get("1.0", END)[:-1].split("&")
    Demo.config(state=NORMAL)
    Demo.delete('1.0', END)
    Demo.insert("end", text[0])
    for i in range(1, len(text)):
        if text[i][0] in colormap:
            Demo.insert("end", text[i][1:], text[i][0])
        else:
            Demo.insert("end", text[i], text[i - 1][0])
    Demo.config(state=DISABLED)


window = Tk()
window.title("ColorMes")
window.geometry("614x240")
window.resizable(width=False, height=False)
try:
    window.iconbitmap("icon.ico")
except:
    pass


InputText = Label(window, text="Ваш текст")
InputText.place(x=2, y=9)
InputText.configure(font=("F77 Minecraft", 10))
Input = Text(window)
Input.place(x=5, y=30, width=604, height=50)
Input.configure(font=("F77 Minecraft", 8), bg="gray75")

DemoText = Label(window, text="Предпросмотр")
DemoText.place(x=2, y=87)
DemoText.configure(font=("F77 Minecraft", 10))
Demo = Text(window)
Demo.place(x=5, y=110, width=604, height=50)
Demo.configure(font=("F77 Minecraft", 8), bg="gray75")
for c in colormap:
    Demo.tag_config(c, foreground=colormap[c])
Demo.config(state=DISABLED)

start = Button(window, text="Просмотр", command=clicked)
start.place(x=20, y=180, width=100, height=50)
start.configure(font=("F77 Minecraft", 10))

copyt = Button(window, text="Скопировать", command=copy)
copyt.place(x=140, y=180, width=130, height=50)
copyt.configure(font=("F77 Minecraft", 10))

clear = Button(window, text="Очистить", command=delete)
clear.place(x=290, y=180, width=100, height=50)
clear.configure(font=("F77 Minecraft", 10))

urll = Button(window, text="GitHub", command=url)
urll.place(x=410, y=180, width=80, height=50)
urll.configure(font=("F77 Minecraft", 10))

forr = Button(window, text="Forum", command=forum)
forr.place(x=510, y=180, width=80, height=50)
forr.configure(font=("F77 Minecraft", 10))

window.mainloop()
