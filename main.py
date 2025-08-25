import pyAesCrypt
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import filedialog as fd
from tkinter import ttk
from random import randint
import pyperclip

password = ""
put = ""
name = ""
alth_pass = "1234567890-=qwertyuiopasdfghjkl:zxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]~!@#$%^&*())_+?/"



def encrypt_file():

    clear_window()
    
    if len(password) > 0:
        lbl = Label(window,text="Encryption...",font=("Arial", 14))
        lbl.pack(expand=True)

        try:
            pyAesCrypt.encryptFile(put, f"{put}.aes", password)
            showinfo(title="Info", message="Encryption was successful")
        except:
            showerror(title="Error", message="File encryption failed")

        home()
    else:
        showerror(title="Error", message="Incorrect password")
        home()


def decrypt_file():
 
    clear_window()

    if len(password) > 0:
        lbl = Label(window,text="Decoding...",font=("Arial", 14))
        lbl.pack(expand=True)

        try:
            pyAesCrypt.decryptFile(put, f"{put[:-3:]}", password)
            showinfo(title="Info", message="The decryption was successful.")
        except:
            showerror(title="Error", message="File encryption failed")

        home()
    else:
        showerror(title="Error", message="Incorrect password")
        home()


def size():
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 3
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3

    return (x,y)


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
     

def encrypt_window():

    def entr():
        global password
        password = entry.get()
        encrypt_file()


    clear_window()

    if name[-3:] == "aes":
        showwarning(title="Warning", message="The file is already encrypted, re-encrypting it may damage the file!")


    lbl = Label(window,text="Create a password:",font=("Arial", 14))
    lbl.pack(anchor="n",padx=20, pady=5)

    entry = ttk.Entry()
    entry.pack(anchor="n", padx=20, pady=5)
    


    btn = ttk.Button(text=" Encrypt ", command=entr)
    btn.pack(anchor="n",padx=20, pady=5)  

    btn = ttk.Button(text="     Back     ", command=home)
    btn.pack(anchor="n",padx=20, pady=5)


    
def decrypt_window():

    def entr():
        global password
        password = entry.get()
        decrypt_file()

    clear_window()

    lbl = Label(window,text="Enter password:",font=("Arial", 14))
    lbl.pack(anchor="n",padx=20, pady=5)

    entry = ttk.Entry()
    entry.pack(anchor="n", padx=20, pady=5)
    

    btn = ttk.Button(text=" Decipher ", command=entr)
    btn.pack(anchor="n",padx=20, pady=5)  

    btn = ttk.Button(text="     Back     ", command=home)
    btn.pack(anchor="n",padx=20, pady=5)


def btn_file_poisk():

    global put,name
    put = ""
    name = ""

    clear_window()
    filename = fd.askopenfilename()
    put = filename
    
    
    if filename == "":
        home()
    else:
        for i in range(len(filename)):
            if filename[i*-1] != "/" : 
                name+=filename[i*-1] 
            else:
                break
        name = name[::-1][:-1:]   





        lbl = Label(window, text=f"Select an action for {name} :",font=("Arial", 14))  
        lbl.pack(anchor="n",padx=20, pady=20)

        btn = ttk.Button(text="  Encrypt  ", command = encrypt_window)
        btn.pack(anchor="n",padx=20, pady=5)
        btn = ttk.Button(text=" Decipher ", command=decrypt_window)
        btn.pack(anchor="n",padx=20, pady=5)      
        
        btn = ttk.Button(text="     Back     ", command=home)
        btn.pack(anchor="n",padx=20, pady=5)


def gen_pas():
    def write_buf():
        pyperclip.copy(pas) 
        pyperclip.paste()

    clear_window()

    pas = ""
    for i in range(15):
        pas+=alth_pass[randint(1,len(alth_pass)-1)]

    lbl = Label(window, text="Generated password:",font=("Arial", 14))  
    lbl.pack(anchor="n",padx=20, pady=20)

    lbl = Label(window, text=f"{pas}",font=("Arial", 12))  
    lbl.pack(anchor="n",padx=20, pady=5)

    btn = ttk.Button(text="     Copy     ", command=write_buf)
    btn.pack(anchor="s",padx=20, pady=3)

    btn = ttk.Button(text="     Back     ", command=home)
    btn.pack(anchor="s",padx=20, pady=55)


def info():
    clear_window()

    lbl = Label(window, text="pyAesCrypt v6.1.1",font=("Arial", 10))  
    lbl.pack(anchor="nw",padx=20, pady=5)
    lbl = Label(window, text="FileKey v0.1",font=("Arial", 10))  
    lbl.pack(anchor="nw",padx=20, pady=5)  
    lbl = Label(window, text="Python v3.13.7",font=("Arial", 10))  
    lbl.pack(anchor="nw",padx=20, pady=5)  
    btn = ttk.Button(text="     Back     ", command=home)
    btn.pack(anchor="nw",padx=20, pady=25)


def home():

    clear_window()

    lbl = Label(window, text="Select a file to encrypt or decrypt:",font=("Arial", 14))  
    lbl.pack(anchor="n",padx=20, pady=20)
    btn = ttk.Button(text=" Select file ",width=20, command=btn_file_poisk)
    btn.pack(anchor="n",padx=20, pady=5)
    btn = ttk.Button(text="generate password",width=20, command=gen_pas)
    btn.pack(anchor="n",padx=20, pady=5)
    btn = ttk.Button(text="info",width=20, command=info)
    btn.pack(anchor="n",padx=20, pady=5)



window = Tk()
window.title("FileKey")
icon = PhotoImage(file = "data\icon.png")
window.iconphoto(True, icon)
window.geometry("600x300")
window.wm_geometry("+%d+%d" % size())
home()

window.mainloop()


