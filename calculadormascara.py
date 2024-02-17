from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk
import os
from ttkthemes import ThemedTk

class calculadoraRED:
    def __init__(self, root):
        self.root=self
        self.root.title=('RedApp')
        self.root.geometry('800x600')
        self.root.set_theme('equilux')  
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        #self.create_result_frame()

    def create_labels_and_entries(self):
        Label(self.root, text="Ingrese La máscara en formato Slash").grid(row=2, column=0, pady=10, padx=10)
        self.texto = Text(self.root, height=1, width=10)
        self.texto.grid(row=2, column=1, sticky='w', pady=10, padx=10)
        self.texto.bind('<KeyRelease>', self.check_entries)

    def create_buttons(self):
        self.btn1 = ttk.Button(self.root, text="Abrir", command=self.mascara, state='disabled')
        self.btn1.grid(row=2, column=2, sticky='w', pady=10, padx=10)
     




    def mascaraRed(self):
        x = int(self.texto.get("1.0", "end"))
        if x < 33  and x > -1:

            # Calcula los octetos completos y los bits adicionales
            octetos_completos = x // 8
            bits_adicionales = x % 8

            # Construye la máscara de red
            mascara = [255] * octetos_completos

            if bits_adicionales > 0:
                valor_bits_adicionales = 2 ** (8 - bits_adicionales) - 1
                mascara.append(valor_bits_adicionales)
        
            # Completa la máscara de red con ceros
            while len(mascara) < 4:
                mascara.append(0)
        
            #respuesta.delete(0, END)

            #respuesta.insert(10,".".join(map(str, mascara)))
            ##return ".".join(map(str, mascara))
        else:
            mascara = "el máximo valor de máscara es 32 y el minimo es 0"
            #respuesta.delete(0, END)
            #respuesta.insert(10,mascara)
    

    











if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = calculadoraRED(root)
    root.mainloop()





