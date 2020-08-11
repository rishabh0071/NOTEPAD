from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Notepad")
    file=None
    TextArea.delete(1.0,END)
    

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

    
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("file saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()


def quitApp():
    root.destroy()
    pass
def cut():
    TextArea.event_generate("<<Cut>>")
    pass
def copy():
    TextArea.event_generate("<<Copy>>")
    pass
def paste():
    TextArea.event_generate("<<Paste>>")
    pass
def about():
    showinfo("Notepad","Notepad by Code with RISHABH MAHAJAN")
    pass


if __name__=='__main__':
    

    root=Tk()
    root.title("Notepad")
    root.geometry("700x600")


    #add text area

    TextArea=Text(root, font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    

    #lets create menubar

    MenuBar=Menu(root)

    #file Menu starts 

    FileMenu=Menu(MenuBar, tearoff=0)

    #to open new file

    FileMenu.add_command(label="New", command=newFile)

    #to open already existing file

    FileMenu.add_command(label="Open", command=openFile)

    #to save current file

    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    #file menu ends

    #edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)

    #to give feature a cut, copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    
    EditMenu.add_command(label="Copy",command=copy)
    
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    #edit menu ends

    #help menu starts

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="about Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    #help menu ends



    root.config(menu=MenuBar)

    #adding scrollbar

    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)





    root.mainloop()    