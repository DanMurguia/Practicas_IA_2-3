from tkinter import *
import tkinter as tk
import dibujo_estrella as dibujo

class MenuObjetivos(tk.Toplevel):
    def __init__(self, parent, parametros, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.parent = parent
        self.parametros_inicio = parametros
        self.parent.title("MINTRIS")
        self.parent.geometry("680x500")
        self.configure(bg='#6B0002')
        self.var_ekis1= IntVar()
        self.var_ye1= IntVar()
        self.var_ekis2= IntVar()
        self.var_ye2= IntVar()
        
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)
        
        lblmod = tk.Label(self, text="Ingrese el objetivo 1",
                          font=('Arial',18,'bold italic')
                          ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=3, padx=10 ,pady=15)
        
        lblmod = tk.Label(self, text="X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=2,column=0,padx=50 ,pady=15,)
        
        self.ekis = tk.Entry(self, width = 3,textvariable=self.var_ekis1,
                             font=('Arial',14))
        self.ekis.grid(row=2, column=0,columnspan=2)

        lblmod = tk.Label(self, text="Y:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=2,column=1 ,pady=15)
        
        self.ye = tk.Entry(self, width = 3,textvariable=self.var_ye1,
                             font=('Arial',14))
        self.ye.grid(row=2, column=1,columnspan=2)
        
        lblmod = tk.Label(self, text="Ingrese el objetivo 2",
                          font=('Arial',18,'bold italic')
                          ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=3,column=0,columnspan=3, padx=10 ,pady=15)
        
        lblmod = tk.Label(self, text="X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=0,padx=50 ,pady=15,)
        
        self.ekis = tk.Entry(self, width = 2,textvariable=self.var_ekis2,
                             font=('Arial',14))
        self.ekis.grid(row=4, column=0,columnspan=2)

        lblmod = tk.Label(self, text="Y:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=1 ,pady=15)
        
        self.ye = tk.Entry(self, width = 2,textvariable=self.var_ye2,
                             font=('Arial',14))
        self.ye.grid(row=4, column=1,columnspan=2)
                
        btn_Descifrar = tk.Button(self, text="Jugar", 
                               bg='#4B7D23',width=10,height = 2, command=self.jugar,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=9,column=0,columnspan=3,pady=20)
        
        
        
    def jugar(self):
        j1= self.var_ekis1.get()
        i1= self.var_ye1.get()
        j2= self.var_ekis2.get()
        i2= self.var_ye2.get()
        self.parametros_inicio['j1'] = j1
        self.parametros_inicio['i1'] = i1
        self.parametros_inicio['j2'] = j2
        self.parametros_inicio['i2'] = i2
        print(self.parametros_inicio)
        dibujo.dibujar(self.parametros_inicio)
        return
