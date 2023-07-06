from tkinter import *


root = Tk()
root.title('Sua Calculadora')
root.geometry('408x355')
root.minsize(408,255)
root.maxsize(408,355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#funções operadores
def botao_divisao():
    return 
def botao_click():
    return
def botao_multiplicao():
    return
def botao_subtracao():
    return
divide = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)
#pirmiera fileira
um = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)
dois = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)
tres = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)
multiplica = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)
divide = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=1, column=2)
quatro = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)
cinco = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)
seis = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)
menos = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
menos.grid(row=1, column=2)
sete = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
sete.grid(row=1, column=2)
oito = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
oito.grid(row=2, column=4)
nove = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activebackground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
nove.grid(row=2, column=4)
root.mainloop()
