import tkinter
from PIL import ImageTk, Image 

win = tkinter.Tk()
win.title('Title')

win.resizable(True, True)

win.iconbitmap('pathToFavicon')

# Create label (text)
label1 = tkinter.Label(win, text='That is first label')
label1.pack()   # If .pack() enabled then .grid() will not work ang get an error

label2 = tkinter.Label(win, text='That is second label')
label2.grid(row=0, column=1)

# Create button
button1 = tkinter.Button(win, text='ClickOnButton', state=tkinter.DISABLED, padx=50, pady=50, command=funcName, fg='blue', bg='#fffeee')     # Create button. state is optional, padx and pady is optional, 'command' what do when click on button (optional), 'fg' set color to button's font color (optional), 'bg' set color to button's backgraund color (optional)
button1.grid(row=2, column=1, columnspan=3, rowspan=3)

# Create text input
entry = tkinter.Entry(win, width=100, borderwidth=20, bg='blue', fg='white')
entry.pack()

# Create text input with value submition
entry = tkinter.Entry(win, width=100, borderwidth=5, bg='blue', fg='white')
entry.pack()
entry.insert(0, 'Enter what you want')

def submit():
    inputValue = entry.get()    # Get value from input form
    buttonLabel = tkinter.Label(win, text=inputValue)
    buttonLabel.pack()


button = tkinter.Button(win, text='Submit', command=submit)
button.pack()

# Text input: clear, delete, insert
entry = tkinter.Entry(win)
entry.get()                     # Get value of input
entry.delete(0, tkinter.END)    # Clear value of input
entry.insert(0, 'value')        # Insert value to input

# Exit button
button = tkinter.Button(win, text='Exit', command=win.quit)

# Add backgound image on window
bgImage = ImageTk.PhotoImage(Image.open(r'/home/farhad/Pictures/Amulet.png'))
bgImageLabel = tkinter.Label(image=bgImage)
bgImageLabel.pack()

# Remove Image, label and so on from window
bgImageLabel.pack_forget()  # If you use .pack() before then you should use this properties
button1.grid_forget()       # If you use .grid() before then you should use this properties

# Additional options:
textLabel = tkinter.Label(win, text='Label for take all width', bd=5, relief=tkinter.SUNKEN, anchor=tkinter.E)  # 'bd' = border, 'relief' = рельеф, 'anchor' = position can be East(E) West(W) North(N) South(S) and so on (EN, ES, WN, WS)
textLabel.grid(row=1, column=0, sticky=tkinter.W + tkinter.E)   # 'sticky' = resize the object and by default position is center. Position modified by 'anchor' property in previous example

# Add frame (window inside window)  # You can use .pack() inside frame ever you use .grid() in root window, and vice versa.
frame = tkinter.LabelFrame(win, text='Frame Title', padx=10, pady=10)
frame.grid(padx=5, pady=5)

frameButton = tkinter.Button(frame, text='Button in frame', command=frame.quit)
frameButton.pack()

# Add radiobutton
varName = tkinter.IntVar()      # You always should select type of object. You can you BooleanVar(), StrVar(), DoubleVar(), IntVar()
varName.set(3)                  # By default always 0 selected if IntVar() use

def radioButtonClick(value):
    label = tkinter.Label(win, text='You select ' + str(value))
    label.pack()

tkinter.Radiobutton(win, text='Option 1', variable=varName, value=1, command=lambda: radioButtonClick(varName.get())).pack()
tkinter.Radiobutton(win, text='Option 2', variable=varName, value=2, command=lambda: radioButtonClick(varName.get())).pack()

# Add prompt boxes
from tkinter import messagebox  
messagebox.showinfo('This is info window', 'Information text')
messagebox.showerror('This is error window', 'Error text')
messagebox.showwarning('This is warning window', 'Warning text')
messagebox.askokcancel('Approve or Not', 'Text')
messagebox.askquestion('Will you answer to question?', 'text')  
messagebox.askyesno('Will you answer to question?', 'text')     # For more prompt box types you can find in google or through VisualStudio helper

# Add second window
secondWindow = tkinter.Toplevel()   # Open second window
secondWindow.destroy()      # Close only second window

# Create browse functionality
from tkinter import filedialog


def openImage():
    global myImg
    win.filename = filedialog.askopenfilename(initialdir='/home/$USER', title='Select an image', filetypes=(('png files', '*.png'),('all files', '*.*')))
    tkinter.Label(win, text=win.filename).pack()
    myImg = ImageTk.PhotoImage(Image.open(win.filename))
    tkinter.Label(image=myImg).pack()


openImgBtn = tkinter.Button(win, text='Select image', command=openImage)
openImgBtn.pack()

# Set size to window
win.geometry('400x400')

# Add scale line
position = tkinter.Entry(win)
position.pack()
def scaleShow(pos):
    position.delete(0, tkinter.END)
    position.insert(0, pos)


scaleVLine = tkinter.Scale(win, from_=0, to=100, command=scaleShow)
scaleHLine = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, command=scaleShow)
scaleVLine.pack()
scaleHLine.pack()

# Checkbox
checkBoxVar_1 = tkinter.IntVar()
checkBox_1 = tkinter.Checkbutton(win, text='First Option', variable=checkBoxVar_1)  # .get() will return 0 or 1
checkBox_1.pack()
checkBox_1.select()     # Select by default

checkBoxVar_2 = tkinter.StringVar()
checkBox_2 = tkinter.Checkbutton(win, text='Second Option', variable=checkBoxVar_2, onvalue='PowerOn', offvalue='PowerOff') # .get() will return text in properties that you write
checkBox_2.pack()
checkBox_2.deselect()   # Deselect by default

# Drop-down menu
selectList = [
    'Ponedelnik',
    'Wtornik',
    'Sreda',
    'Cetverq',
    'Pyatnisa',
    'Subbota',
    'Voskresenie'
]

clicked = StringVar()
clicked.set(selectList[0])

selector = tkinter.OptionMenu(win, clicked, *selectList)
selector.pack()     # You can get value with .get() propertie

# Copy to Clipboard
win.clipboard_clear()                           # Clear clipboard if you need it
win.clipboard_append('text copy to clipboard')  

win.mainloop()