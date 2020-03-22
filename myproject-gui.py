'''import tkinter as tk
root = tk.Tk()
w = tk.Label(root, text="Hello Tkinter!")
w.pack()
root.mainloop()
'''

'''from tkinter import *
from tkinter.messagebox import showinfo
class mygui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        but=Button(self,text='press',command=self.reply)
        but.pack()
    def reply(self):
        showinfo(title='popup',message='butttom pressed')
if __name__=='__main__':
    popup=Toplevel()
    window=mygui(popup)
    window.pack()
    window.mainloop()
'''


'''  from tkinter import *
from tkinter.messagebox import showinfo
def reply(name):
    showinfo(title='reply',message='hello %s!!!'%name)

top=Tk()
top.title('Echo')
top.iconbitmap('gmail.ico')
Label(top,text='enter your name:').pack(side=TOP)
e=Entry(top)
e.pack(side=TOP)
Label(top,text='enter key').pack(side=TOP)
e1=Entry(top)
e1.pack(side=TOP)
Label(top,text='enter age').pack(side=TOP)
e2=Entry(top)
e2.pack(side=TOP)
Label(top,text='enter job').pack(side=TOP)
e3=Entry(top)
e3.pack(side=TOP)
Label(top,text='enter pay').pack(side=TOP)
e4=Entry(top)
e4.pack(side=TOP)
btn=Button(top,text='press',command=(lambda:reply(e.get())))
btn.pack(side=TOP)
top.mainloop()
'''

