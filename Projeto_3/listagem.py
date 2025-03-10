from tkinter import * 
from tkinter import ttk

def cadastrar_aluno():
    tv.insert('','end',values=(vnome.get(), vemail.get(), vcurso.get()))
    vnome.delete(0,END)
    vemail.delete(0,END)
    vcurso.delete(0,END)

app = Tk()  
app.title("ADS - Fecaf")
app.geometry("600x450")

lbnome = Label(app, text="Nome")
vnome = Entry(app)

lbemail = Label(app, text="Email")
vemail= Entry(app)

lbcurso= Label(app, text="Curso")
vcurso= Entry(app)

tv = ttk.Treeview(app, columns=("Nome" , "Email", "Curso"), show="headings")

tv.column('Nome', minwidth=0, width=250)
tv.column('Email', minwidth=0, width=210)
tv.column('Curso', minwidth=0, width=100)

tv.heading('Nome', text="NOME")
tv.heading('Email', text="E-MAIL")
tv.heading('Curso', text="CURSO")

btncadastrar = Button(app, text="Cadastrar", command=cadastrar_aluno)

lbnome.grid(column=0, row=0, sticky="W")
vnome.grid(column=0, row=1)


lbemail.grid(column=1, row=0, sticky="W")
vemail.grid(column=1, row=1)

lbcurso.grid(column=2, row=0, sticky="W")
vcurso.grid(column=2, row=1)

btncadastrar.grid(column=3,row=1)
tv.grid(column=0, row=2, columnspan=4)


app.mainloop()
