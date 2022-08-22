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


win.mainloop()