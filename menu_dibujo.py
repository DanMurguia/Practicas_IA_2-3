from tkinter import *
import tkinter as tk
from tkinter import filedialog
import dibujo


class MenuDibujo(tk.Toplevel):
    def __init__(self, parent,parametros, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parametros_inicio = parametros
        self.parent.title("MINTRIS")
        self.parent.geometry("680x500")
        self.configure(bg='#6B0002')
        self.var_tipo_dibujo = IntVar()

    
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)        
        
        lblmod = tk.Label(self, text="Seleccione un estilo de dibujo",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=3,padx =10 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Paso por paso', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',
                           variable=self.var_tipo_dibujo)
        rad0.grid(row=2, column=0)
        
        rad1 = Radiobutton(self,text='Nodo por nodo', value=2 ,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',
                           variable=self.var_tipo_dibujo)
        rad1.grid(row=2, column=1) 
                
        btn_Descifrar = tk.Button(self, text="Jugar", 
                               bg='#4B7D23',width=10,height = 2, command=self.jugar,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=3,column=0, columnspan=2,pady=20)
        
        
    def jugar(self):
        tipo_dibujo = self.var_tipo_dibujo.get()
        if tipo_dibujo:
            self.parametros_inicio['dibujo']=tipo_dibujo
            print(self.parametros_inicio)
            dibujo.dibujar(self.parametros_inicio)
        else:
            messagebox.showinfo(message="Seleccione un estilo de dibujo")
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
