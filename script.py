import tkinter
from PIL import ImageTk, Image 


win = tkinter.Tk()
win.title('MyPage')

bgImage = ImageTk.PhotoImage(Image.open(r'/home/farhad/Pictures/Amulet.png'))
bgImageLabel = tkinter.Label(image=bgImage)
bgImageLabel.pack()

button = tkinter.Button(win, text='Submit', command=win.quit)
button.pack()


win.mainloop()
