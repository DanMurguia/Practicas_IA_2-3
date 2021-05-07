from tkinter import *
import tkinter as tk
from tkinter import filedialog
import dibujo 


class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("MINTRIS")
        self.parent.geometry("505x630")
        self.configure(bg='#6B0002')
        self.filename = ""
        self.var_key = StringVar()
        self.var_iv = StringVar()
        self.var_ente = IntVar()
        self.var_ekis = IntVar()
        self.var_ye = IntVar()
        self.var_modo = IntVar()
        self.ivname=""
        self.imagen = []
        self.img_enc = []
        self.cabecera = []
    
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)        
        
        lblmod = tk.Label(self, text="Seleccione un personaje",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=2,padx =10 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Humano', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad0.grid(row=2, column=0)
        
        rad1 = Radiobutton(self,text='Mono', value=3,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad1.grid(row=2, column=1) 
        
        rad2 = Radiobutton(self,text='Pulpo', value=2,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad2.grid(row=2, column=2)

        rad3 = Radiobutton(self,text='Sasquach', value=4,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad3.grid(row=3, column=1, pady=15)
        
                
        lblmod = tk.Label(self, text="Seleccione un modo",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=0,columnspan=2 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Manual', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad0.grid(row=5, column=0)
        
        rad1 = Radiobutton(self,text='Automatico', value=2,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad1.grid(row=5, column=1)
        
        lblmod = tk.Label(self, text="Ingrese las coordenadas de inicio",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=6,column=0,columnspan=3 ,pady=15)
        
        lblmod = tk.Label(self, text="X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=7,column=0 ,pady=15)
        
        self.ekis = tk.Entry(self, width = 5,textvariable=self.var_ekis,
                             font=('Arial',14))
        self.ekis.grid(row=7, column=1)

        lblmod = tk.Label(self, text="Y:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=8,column=0 ,pady=15)
        
        self.ye = tk.Entry(self, width = 5,textvariable=self.var_ye,
                             font=('Arial',14))
        self.ye.grid(row=8, column=1)
                
        btn_Descifrar = tk.Button(self, text="Jugar", 
                               bg='#4B7D23',width=10,height = 2, command=self.jugar,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=9,column=1,pady=20)
        
        
    def jugar(self):
        ente = self.var_ente.get()
        modo = self.var_modo.get()
        x = self.var_ekis.get()
        y = self.var_ye.get()
        if ente and modo:
            dibujo.dibujar(ente,modo,x,y)
        else:
            messagebox.showinfo(message="Seleccione un personaje y un modo")
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
