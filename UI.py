import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    #path2.insert(END, filename)
    im = Image.open(filename)


    im = im.resize((320, 320))
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(frame, image=tkimage)
    myvar.image = tkimage

    myvar.place(x=730, y=50)
    print('Selected:', filename)


def UploadAction1(event=None):
    filename1 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    #pathh.insert(END, filename1)
    filename1 = open(filename1, 'r')
    data = filename1.read()
    txtarea.insert(END, data)
    filename1.close()
    print('Selected:', filename1)

root = tk.Tk()
root.geometry("400x450")
root['bg'] = '#fb0'

txtarea = Text(root, width=40, height=20)
txtarea.pack(pady=50)

# pathh = Entry(root)
# pathh.pack(side=LEFT, expand=True, fill=X, padx=10)
# path2= Entry(root)
# path2.pack(side=LEFT, expand=True, fill=X, padx=10)






root.geometry("1090x700")
var = StringVar()
var2 = StringVar()
frame = Frame(root).place(x=40, y=600)
canvas = Canvas(root)
canvas.create_line(300, 35, 300, 200, dash=(5, 2))

First_file = Label(root, text="STEGENOGRAPHY ENCRYPTION", font=("Times New Roman", 18)).place(x=350, y=10)

First_file = Label(root, text="Select the Picture to Hide", font=("Times New Roman", 11)).place(x=40, y=150)
Second_file = Label(root, text="Select the file to be encrypted", font=("Times New Roman", 11)).place(x=40, y=70)

# text=Text(root).place(x=400,y=70)


button = tk.Button(root, text='Select', command=UploadAction).place(x=240, y=150)
button2 = tk.Button(root, text='Select', command=UploadAction1).place(x=240, y=70)

root.mainloop()

