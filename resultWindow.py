from tkinter import *
from tkinter.messagebox import showinfo



class CopyLabel(Tk):
    def __init__(self, text: str):
        super(CopyLabel, self).__init__()

        self.title('Your Password ^_^ :')

        width=500
        height=150
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)


        self.label_text = text
        self.label = Label(self, text=text)
        self.label.pack(pady=10, padx=40)

        self.copy_button = Button(self, text='Copy The Password', command=self.copy)
        self.close_button = Button(self, text = 'Close Window', command=self.close)
        self.copy_button.pack(pady=5, padx=40)
        self.close_button.pack(pady=5, padx=40)

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.label_text)

        self.update()

        showinfo(parent=self, message='Password has been copied!')
    
    def close(self):
        self.destroy()


def showPassword(password):
    print("ISIDE NOW ====================== ")
    app = CopyLabel(password)
    app.mainloop()

