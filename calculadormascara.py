from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk
import os
from ttkthemes import ThemedTk

class calculadoraRED:
    def __init__(self, root):
        self.root = root
        self.root.title('Compi App')
        self.root.geometry("900x600")
        #self.root.config(background="white")
        self.root.set_theme('equilux')  
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        #framemascara
        self.nav_bar = ttk.Frame(self.root, height=50)
        self.nav_bar.pack(fill='x')
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        #self.create_result_frame()

    def create_labels_and_entries(self):
        
        Label(self.nav_bar, text="Ingrese La máscara en formato Slash", bg="#3b5998", fg="white").pack(side='left', pady=10, padx=10)
        self.texto = Text(self.nav_bar, height=1, width=20)
        self.texto.pack(side='left', pady=10, padx=10)

    
    
    def create_buttons(self):
            # Colocar el botón dentro del nav_bar
            self.btn1 = ttk.Button(self.nav_bar, text="convertir", command=self.mascaraRed)
            self.btn1.pack(side='left', padx=10)  # Ajusta según tus preferencias
     




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
    root = ThemedTk(theme="equilux")
    app = calculadoraRED(root)
    root.mainloop()





