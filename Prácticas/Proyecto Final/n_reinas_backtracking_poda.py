from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import ressagebox
from PIL import *
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import as
import sys
import numpy as np


x=0
a=1

def checkQueens(queens, n, k):
    for i in range(0, k):
        if((queens[i]==queens[k]) or (abs(k-i)==abs(queens[k]-queens[i]))):
            return False
    return True

def NQueens(queens, n, k, dictSolutions):
    if(k==n):
        global x
        x=x+1
        sol=[]
        for i in range(0, n):
            sol.append(queens[i])
        dictSolutions[x] = {
            x:sol
        }
    
    else:
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1, dictSolutions)
 
def window():
    root=Tk()
    root.geometry('1024x700')
    root.title('N Reinas')
    root.resizable(0,0)
    
    mainTitle=ttk.Label(root, text="Problema de las N Reinas")
    mainTitle.pack()
    mainTitle.config(font=('Arial',18))
    Label(root, text=" ").pack()
    txtEntryQueens = ttk.Label(root, texto="Ingrese el número de reinas: ")
    txtEntryQueens.pack()
    txtEntryQueens.config(font=('Arial',12))
    entryQueens = ttk.Entry(root) 
    entryQueens.pack()
    entryQueens.config(font=('Arial',12), justify=("center"))
    s=ttk.Style()
    s.configure(
        "MyNutton.TButton"
        font=("Arial",12)
        background="#000000"
    )
     
def printBoard(m, dictSolutions, a, fig, ax, canvas):
    txtRes=ttk.Label(root, text=f'Solución {a}')
    txtRes.config(font=('Arial',12))
    txtRes.pack()
    
    array=dictSolutions[a][a]
    colors=['black','red','yellow','blue','pink','green','violet','cyan','brown','orange']
    
    ax.clear()
    ax.axis('off')
    ax.tick_parms(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    
    for i in range(0,m):
        if array[i] != -1:
            ax.plot([i+0.5],[array[i]+0.5], marker="*",markersize=20,color=f'{colors[i]}')
    plt.tight_leyout()
    ax.patch.set_visible(False)
    canvas.draw()
    canvas.get_tk_widget().pack()
    a+=1     
                
def callQueens():
    k=0
    global a
    dictSolutions = {}
    n = entryQueens.get()
    if n.isdigt():
        m=int(n)
        if(m>3 and m<11):
            queens=[-1 for n in range(0,m)]
            numSol = NQueens(queens, m, k, dictSolutions)
            entryQueens['state']= DISABLED
            btnQueens['state']=DISABLED
            Label(root,text=" ").pack()
            labelSolutions=ttk.Label(root, text=f'Total de soluciones: {x}')
            labelSolutions.pack()
            labelSolutions.config(font=('Arial',12))
            view=ttk.Label(root,text="ingrese el número de solución que desea ver: ")
            view.pack()
            view.config(font=('Arial',12))
            txtView=ttk.Entry(root)
            txtView.pack()
            txtView.config(font=('Arial',12),justify=("center"))
            
            def verify(m, dictSolutions):
                a=txtView.get()
                if a.isdigit():
                    b=int(a)
                    if(b>0 and b<=x):
                        printBoard(m, dictSolutions,n,fig,ax,canvas)
                        txtView.delete("0","end")
                    else:
                        messagebox.showinfo(f'Mayor a 0',f'El número debe ser mayor a 0 y menor a {x+1}')
                        txtView.delete("0","end")
                    else:
                        messagebox.showinfo(f'Solo números',f'Solo se permiten números')
                        txtView.delete("0","end")
                fig = Figure(figsize=(5,5))
                ax=fig.add_subplot(111)
                canvas=FigureCanvasTkAgg(fig,root)
                btnView=ttk.Button(root, text="ver", style="MyButton.TButton",command=lambda:verify(m,dictSolutions))
                btn.View.pack()
        else:
            messagebox.showinfo(f'Mayor a 3',f'El número debe ser mayor a 3 y menor a 11')
            txtView.delete("0","end")
        else:
            messagebox.showinfo(f'Solo números',f'Solo se permiten números mayores a 3')
            txtView.delete("0","end")
    btnQueens=ttk.Button(root,text="Generar",style="MyButton.TButton",command=callQueens)
    btnQueens.pack()
    
    def restart():
        os.execl(sys.executable, sys.executable, * sys.argv)
    btnExit=ttk.Button(root,text='Limpiar',command=restart,style="MyButton.TButton")
    btnEXIT.PACK(SIDE=BOTTOM)
    root.mainloop()
    
window()    
                        