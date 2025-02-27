import tkinter as tk  
from tkinter import ttk  

app = tk.Tk()  

app.title("ADS - Fecaf")
app.geometry("600x450")

# Widgets
lbnome = tk.Label(app, text="Nome")
vnome = tk.Entry(app)
lbemail = tk.Label(app, text="Email")
vemail = tk.Entry(app)

lbcurso = tk.Label(app, text="Curso")
vcurso = tk.Entry(app)

tv = ttk.Treeview(app,columns=("nome", "email", "curso"))
tv.column("nome", minwidth=0)


app.mainloop()
