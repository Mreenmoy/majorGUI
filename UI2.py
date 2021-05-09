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

    passwordlab = Label(root, text="Password", font=("Times New Roman", 11)).place(x=40, y=250)
    e1 = tk.Entry(root, show="*", font=('Arial', 14)).place(x=120, y=250)
    button3 = tk.Button(root, text='ENCRYPT', command=encrytingaction,width =10 ,height =4).place(x=150, y=300)
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

def encrytingaction(event=None):#callencrytingfucntion
    encryptwin = Toplevel(root)
    encryptwin.title("ENCRYPTED OUTPUT")
    encryptwin.geometry("900x700")
    encryptwin.config(bg="skyblue")

    left_frame = Frame(encryptwin, width=200, height=400, bg='white')
    left_frame.grid(row=0, column=0, padx=10, pady=5)
    right_frame = Frame(encryptwin, width=650, height=400, bg='white')
    right_frame.grid(row=0, column=1, padx=10, pady=5)
    Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

    tool_bar = Frame(left_frame, width=180, height=185)
    tool_bar.grid(row=2, column=0, padx=5, pady=5)

    button4 = tk.Button(tool_bar, text='DECRYPT', command=decryptingaction).grid(row=0, column=0, padx=10, pady=30,ipadx=10)

    # Label(tool_bar, text="DECRYPT", relief=RAISED).grid(row=0, column=0, padx=10, pady=30,ipadx=10)
    # ipadx is padding inside the Label widget
    # Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)


    Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
    # Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
    # Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
    # Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
    # Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)




def decryptingaction(event=None):#call decrypting fuction
    print()



root = tk.Tk()
root.title("STEGENOGRAPHY ENCRYPTION ")

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



#button4 = tk.Button(root, text='DECRYPT', command=decryptingaction).place(x=180, y=250)


root.mainloop()




#-------------------------
#
# # import tkinter and all its functions
# from tkinter import *
#
# root = Tk()  # create root window
# root.title("Basic GUI Layout")  # title of the GUI window
# root.maxsize(900, 600)  # specify the max size the window can expand to
# root.config(bg="skyblue")  # specify background color
#
# # Create left and right frames
# left_frame = Frame(root, width=200, height=400, bg='grey')
# left_frame.grid(row=0, column=0, padx=10, pady=5)
# right_frame = Frame(root, width=650, height=400, bg='grey')
# right_frame.grid(row=0, column=1, padx=10, pady=5)
#
# # Create frames and labels in left_frame
# Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)
#
# # load image to be "edited"
# image = PhotoImage(file="rain.gif")
# original_image = image.subsample(3, 3)  # resize image using subsample
# Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)
#
# # Display image in right_frame
# Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)
#
# # Create tool bar frame
# tool_bar = Frame(left_frame, width=180, height=185)
# tool_bar.grid(row=2, column=0, padx=5, pady=5)
#
# # Example labels that serve as placeholders for other widgets
# Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3,
#                                                   ipadx=10)  # ipadx is padding inside the Label widget
# Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)
#
# # Example labels that could be displayed under the "Tool" menu
# Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
# Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
# Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
# Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
# Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
#
# root.mainloop()
