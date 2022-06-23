from tkinter import*
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename

import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.8,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                    "Text Document","*.txt"])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.8,END)
        f=open(file,"r")
        TextArea.insert(1.8,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                            filetypes=[("All Files","*.*"),
                                "Text Document","*.txt"])   
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.8,END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("File saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.8,END))
        f.close()
def QuitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<>"))
def copy():
    TextArea.event_generate(("<>"))
def paste():
    TextArea.event_generate(("<>"))
def about():
    showinfo("Notepad","Notepad by Saras ")

if __name__=='__main__':
    root=Tk()
    root.title("Untitle -Notepad")
    root.geometry("644x788")
    TextArea=Text(root,font="lucida 13")        
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    Menubar=Menu(root)
    fileMenu=Menu(Menubar,tearoff=0)
    fileMenu.add_command(label="new",command=newFile)
    fileMenu.add_command(label="open",command=openFile)
    fileMenu.add_command(label="save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=QuitApp)
    Menubar.add_cascade(label="file",menu=fileMenu)
    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="cut",command=cut)
    EditMenu.add_command(label="copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About notepad",command=about)
    Menubar.add_cascade(label="help",menu=HelpMenu)
    root.config(menu=Menubar)
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
    
