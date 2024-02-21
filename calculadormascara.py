from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk
import os
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk

class calculadoraRED:
    def __init__(self, root):
        self.root = root
        self.root.title('Compi App')
        self.root.geometry("900x600")
        
        #estilos de los frames
        style = ttk.Style()
        #style.theme_use("clam")
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='#949494')
        style.configure('Titulo.TLabel', background='#949494', foreground='white', font=('Helvetica', 10))

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=10, columnspan=3)
        #frame lateral izquierda
        self.lateral = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.lateral.grid(row=1, column=0, sticky='ns', padx=10, pady=0, rowspan=4)
        #frame de mascara
        self.mascfr = ttk.Frame(self.root, style='modulo.TFrame')
        self.mascfr = ttk.LabelFrame(self.root, text="Determinar máscara", padding=(20, 20))
        self.mascfr.grid(row=1, column=1, pady=10, padx=10)

        
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        #self.create_result_frame()

    def create_labels_and_entries(self):
        
        Label(self.mascfr, text="Ingrese La máscara en formato Slash sin la barra:",background="#414141", foreground="white").grid(row=1,column=2, pady=10)
        self.texto = Text(self.mascfr, height=1, width=10)
        self.texto.grid(row=2,column=2, pady=10)
        Label(self.mascfr, text='Resultado:', background="#414141", foreground="white").grid(row=3,column=2, pady=10)
        self.resulmasc = Text(self.mascfr, height=1, width=20)
        self.resulmasc.grid(row=4,column=2, pady=10)

    
    
    def create_buttons(self):
        style = ttk.Style()        
        style.configure("Fancy.TButton", foreground="white", background="#0099ff", borderwidth=0)        
        self.btn1 = ttk.Button(self.mascfr, text="convertir", command=self.mascaraRed, style='Fancy.TButton')
        self.btn1.grid(row=5,column=2, pady=10)
     




    def mascaraRed(self):
        x = self.texto.get("1.0", "end-1c")
        x = x.strip("\n")
        x=int(x)
        print(x)
        
        if x < 33  and x > -1:
            
            print('holq')

            # Calcula los octetos completos y los bits adicionales
            octetos_completos = x // 8
            bits_adicionales = x % 8

            # Construye la máscara de red
            self.mascara = [255] * octetos_completos

            if bits_adicionales > 0:
                valor_bits_adicionales = 2 ** (8 - bits_adicionales) - 1
                self.mascara.append(valor_bits_adicionales)
        
            #Completa la máscara de red con ceros
            while len(self.mascara) < 4:
                self.mascara.append(0)
        
            #respuesta.delete(0, END)

            self.resulmasc.insert(10,".".join(map(str, self.mascara)))
        
            return ".".join(map(str, self.mascara))
        else:
            self.mascara = "el máximo valor de máscara es 32 y el minimo es 0"
            self.resulmasc.delete(0, 'END')
            self.resulmasc.insert(10,self.mascara)
    

    











if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = calculadoraRED(root)
    root.mainloop()





