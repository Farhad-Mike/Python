bookmarks = open(r'D:\bookmarks.txt')

newBookmarks = []

completedBookmarks = []

for bookmark in bookmarks:
    if bookmark.find('torrents-igruha.org') != -1:
        newBookmarks.append(bookmark)


for bookmark in newBookmarks:
    position = bookmark.find('torrents-igruha.org')
    completedBookmarks.append('https://' + bookmark[position:])

print(completedBookmarks)

newFile = open(r'D:\newBookmarks.txt', 'w')
newFile.write('')
newFile.close()
newFile = open(r'D:\newBookmarks.txt', 'a')

for _ in completedBookmarks:
    newFile.write(_)


newFile.close()
import tkinter
from tkinter import StringVar, messagebox
from PIL import ImageTk, Image 


win = tkinter.Tk()
win.title('MyPage')

bgImage = ImageTk.PhotoImage(Image.open(r'/home/farhad/Pictures/Amulet.png'))
bgImageLabel = tkinter.Label(image=bgImage)
bgImageLabel.pack()

textLabel = tkinter.Label(win, text='Label for take all width', bd=5, relief=tkinter.SUNKEN, anchor=tkinter.E)
textLabel.pack()


button = tkinter.Button(win, text='Submit', command=win.quit)
button.pack()


frame = tkinter.LabelFrame(win, text='Frame Title', padx=10, pady=10)
frame.pack()

frameButton = tkinter.Button(frame, text='Button in frame', command=frame.destroy)
frameButton.pack()


position = tkinter.Entry(win)
position.pack()
def scaleShow(pos):
    position.delete(0, tkinter.END)
    position.insert(0, pos)


scaleVLine = tkinter.Scale(win, from_=0, to=100, command=scaleShow)
scaleHLine = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, command=scaleShow)
scaleVLine.pack()
scaleHLine.pack()


checkBoxVar_1 = tkinter.IntVar()
checkBox_1 = tkinter.Checkbutton(win, text='First Option', variable=checkBoxVar_1)
checkBox_1.pack()
checkBox_1.select()

checkBoxVar_2 = tkinter.StringVar()
checkBox_2 = tkinter.Checkbutton(win, text='Second Option', variable=checkBoxVar_2, onvalue='PowerOn', offvalue='PowerOff')
checkBox_2.pack()
checkBox_2.deselect()


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
selector.pack()


win.mainloop()
