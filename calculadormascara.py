from tkinter import *
import tkinter as tk
import os

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
        self.create_result_frame()




def calcular_mascara_red():
    x=int(textExample.get(1.0, tk.END+"-1c"))
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
    
        respuesta.delete(0, END)

        respuesta.insert(10,".".join(map(str, mascara)))
        #return ".".join(map(str, mascara))
    else:
        mascara = "el máximo valor de máscara es 32 y el minimo es 0"
        respuesta.delete(0, END)
        respuesta.insert(10,mascara)
    

    


def create_labels_and_entries(self):
    Label(self.root, text="Máscara en octetos").grid(row=2, column=0, pady=10, padx=10)
    self.texto = Text(self.root, height=1, width=10)
    self.texto.grid(row=0, column=1, sticky='w', pady=10, padx=10)
    self.texto.bind('<KeyRelease>', self.check_entries)
     



#creamos la variable entrada y la poscionamos

textExample=tk.Text(root, height=1, width=15, border=5)
textExample.grid(row=1,column=0, padx=15, pady=15)
#textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Calcular", command=calcular_mascara_red)
btnRead.grid(row=5,column=0, padx=15, pady=15)

#btnRead.pack()

label = Label(root, text="RESPUESTA: ")
label.grid(row=2,column=0, padx=15, pady=15)

respuesta = tk.Entry(root)

respuesta.grid(row=3,column=0, padx=15, pady=15)
#respuesta.pack()





root.mainloop()




