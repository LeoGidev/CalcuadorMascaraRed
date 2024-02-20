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
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='#949494')
        #style.configure('Titulo.TLabel', background='#949494', foreground='white', font=('Helvetica', 10))

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.pack(fill='x')
        #frame lateral izquierda
        self.lateral = ttk.Frame(self.root, width=250, style='barratop.TFrame')
        self.lateral.pack(fill='y', side='left')
        #frame de mascara
        self.mascfr = ttk.Frame(self.root, height=250, width=250, style='modulo.TFrame')
        self.mascfr = ttk.LabelFrame(self.root, text="Determinar máscara", padding=(20, 20))
        self.mascfr.pack(side='right', anchor='n')

        
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        #self.create_result_frame()

    def create_labels_and_entries(self):
        
        Label(self.mascfr, text="Ingrese La máscara en formato Slash sin la barra:").pack(side='left', pady=10, padx=10)
        self.texto = Text(self.mascfr, height=1, width=10)
        self.texto.pack(side='left', pady=10, padx=10)
        self.resulmasc = Text(self.mascfr, height=1, width=20)
        self.resulmasc.pack(side="bottom", anchor="center")

    
    
    def create_buttons(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Fancy.TButton", foreground="white", background="#0099ff", borderwidth=0)
        
        #style.configure("TButton", background='black', foreground='black', troughcolor='blue', focuscolor="red", highlightbackground='green', borderwidth=0)
        self.btn1 = ttk.Button(self.mascfr, text="convertir", command=self.mascaraRed, style='Fancy.TButton')
        self.btn1.pack(side='left', padx=10)
     




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
            mascara = [255] * octetos_completos

            #if bits_adicionales > 0:
            valor_bits_adicionales = 2 ** (8 - bits_adicionales) - 1
            mascara.append(valor_bits_adicionales)
        
            #Completa la máscara de red con ceros
            while len(mascara) < 4:
                mascara.append(0)
        
            #respuesta.delete(0, END)

            #respuesta.insert(10,".".join(map(str, mascara)))
            return ".".join(map(str, mascara))
        else:
            mascara = "el máximo valor de máscara es 32 y el minimo es 0"
            #respuesta.delete(0, END)
            #respuesta.insert(10,mascara)
    

    











if __name__ == "__main__":
    root = tk.Tk()
    app = calculadoraRED(root)
    root.mainloop()





