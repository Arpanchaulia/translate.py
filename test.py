from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    # Remove unnecessary variable assignments
    trans = Translator()
    try:
        # Add error handling for translation
        #trans1 = trans.translate(text.strip(), src=src.lower(), dest=dest.lower())
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except Exception as e:
        return f"Translation Error: {str(e)}"

def data():
    try:
        s = comb_sor.get()
        d = comb_dest.get()
        masg = Sor_Txt.get(1.0, END)
        textget = change(text=masg, src=s, dest=d)
        dest_Txt.delete(1.0, END)
        dest_Txt.insert(END, textget)
    except Exception as e:
        dest_Txt.delete(1.0, END)
        dest_Txt.insert(END, f"Error: {str(e)}")
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

Frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=120,height=20,width=300)

Sor_Txt = Text(Frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_Txt.place(x=10,y=150,height=130,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(Frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change=Button(Frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(Frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Dest Text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_Txt = Text(Frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_Txt.place(x=10,y=400,height=150,width=480)



root.mainloop()
