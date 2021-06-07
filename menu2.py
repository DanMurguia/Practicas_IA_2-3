from tkinter import *
import tkinter as tk
import menu_objetivos, menu_dibujo

class Menu2(tk.Toplevel):
    def __init__(self, parent, parametros, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.parent = parent
        self.parametros_inicio = parametros
        self.parent.title("MINTRIS")
        self.parent.geometry("680x500")
        self.configure(bg='#6B0002')
        self.var_ekis_ini = IntVar()
        self.var_ye_ini = IntVar()
        self.var_ekis_fin = IntVar()
        self.var_ye_fin = IntVar()
        
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)
        
        lblmod = tk.Label(self, text="Ingrese las coordenadas de inicio",
                          font=('Arial',18,'bold italic')
                          ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=3, padx=10 ,pady=15)
        
        lblmod = tk.Label(self, text="X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=2,column=0,padx=50 ,pady=15,)
        
        self.ekis = tk.Entry(self, width = 3,textvariable=self.var_ekis_ini,
                             font=('Arial',14))
        self.ekis.grid(row=2, column=0,columnspan=2)

        lblmod = tk.Label(self, text="Y:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=2,column=1 ,pady=15)
        
        self.ye = tk.Entry(self, width = 3,textvariable=self.var_ye_ini,
                             font=('Arial',14))
        self.ye.grid(row=2, column=1,columnspan=2)
        
        lblmod = tk.Label(self, text="Ingrese las coordenadas de fin",
                          font=('Arial',18,'bold italic')
                          ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=3,column=0,columnspan=3, padx=10 ,pady=15)
        
        lblmod = tk.Label(self, text="X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=0,padx=50 ,pady=15,)
        
        self.ekis = tk.Entry(self, width = 2,textvariable=self.var_ekis_fin,
                             font=('Arial',14))
        self.ekis.grid(row=4, column=0,columnspan=2)

        lblmod = tk.Label(self, text="Y:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=1 ,pady=15)
        
        self.ye = tk.Entry(self, width = 2,textvariable=self.var_ye_fin,
                             font=('Arial',14))
        self.ye.grid(row=4, column=1,columnspan=2)
                
        btn_Descifrar = tk.Button(self, text="Siguiente", 
                               bg='#4B7D23',width=10,height = 2, command=self.siguiente,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=9,column=0,columnspan=3,pady=20)
        
        
        
    def siguiente(self):
        j_ini = self.var_ekis_ini.get()
        i_ini = self.var_ye_ini.get()
        j_fin = self.var_ekis_fin.get()
        i_fin = self.var_ye_fin.get()
        self.parametros_inicio['j_inicial'] = j_ini
        self.parametros_inicio['i_inicial'] = i_ini
        self.parametros_inicio['j_final'] = j_fin
        self.parametros_inicio['i_final'] = i_fin
        print(self.parametros_inicio)
        if self.parametros_inicio['modo'] == 4:
            menu_objetivos.MenuObjetivos(self.parent,self.parametros_inicio)
        else:
            menu_dibujo.MenuDibujo(self.parent,self.parametros_inicio)
        return
