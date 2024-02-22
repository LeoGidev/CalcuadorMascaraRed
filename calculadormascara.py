from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk, Scale, Canvas
import os
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import imageio


class calculadoraRED:
    def __init__(self, root):
        self.root = root
        self.root.title('Tecnic Assitant')
        self.root.geometry("900x600")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()
        #style.theme_use("clam")
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='#414141')
        #style.configure('Titulo.TLabel', background='#949494', foreground='white', font=('Helvetica', 10))

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=0, columnspan=3)
        #frame lateral izquierda
        self.lateral = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.lateral = ttk.LabelFrame(self.root, text='Calculos de potencia:', padding=(10,10))
        self.lateral.grid(row=1, column=0, sticky='ns', padx=0, pady=0, rowspan=4)
        #frame de mascara
        self.mascfr = ttk.Frame(self.root, style='modulo.TFrame')
        self.mascfr = ttk.LabelFrame(self.root, text="Determinar máscara:", padding=(20, 20))
        self.mascfr.grid(row=1, column=1, pady=0, padx=0)
        #Frame de Ibuttons
        self.ibut = ttk.Frame(self.root, style='modulo.TFrame')
        self.ibut = ttk.LabelFrame(self.root, text='Convertir IBUTTONS:', padding=(59, 20))
        self.ibut.grid(row=2, column=1, padx=0, pady=10)
        #gif
         # Crea un label para mostrar el gif en la columna 3
        self.gif = ttk.Frame(self.root)
        self.gif.grid(row=1, column=2, rowspan=4, sticky='ns', padx=10)


        
        
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        #self.create_result_frame()

    def create_labels_and_entries(self):
        #labels del convertidor de máscara
        Label(self.mascfr, text="Ingrese La máscara en formato Slash sin la barra:",background="#414141", foreground="white").grid(row=1,column=2, pady=10)
        self.texto = Text(self.mascfr, height=1, width=10)
        self.texto.grid(row=2,column=2, pady=10)
        Label(self.mascfr, text='Resultado:', background="#414141", foreground="white").grid(row=3,column=2, pady=10)
        self.resulmasc = Text(self.mascfr, height=1, width=20)
        self.resulmasc.grid(row=4,column=2, pady=10)
        #Labels del convertidor de IButtons
        Label(self.ibut,text='Ingrese el valor de RFID', background='#414141', foreground='white').grid(row=0, column=1, padx=10, pady=10)
        self.texto2 = Text(self.ibut, height=1, width=20)
        self.texto2.grid(row=1, column=1, padx=10, pady=10)
        Label(self.ibut, text='Resultado:', background='#414141', foreground='white').grid(row=2, column=1, padx=10, pady=10)
        self.resulibut = Text(self.ibut, height=1, width=20)
        self.resulibut.grid(row=3, column=1, padx=10, pady=10)
        #Labels del módulo de potencia
        Label(self.lateral, text='Ingrese corriente consumida en baterías', background='#414141', foreground='white').grid(row=0, column=0, columnspan=2, sticky='ew', padx=0, pady=10)
        self.text2 = Text(self.lateral, height=1, width=10)
        self.text2.grid(row=1,column=0, sticky='e', padx=4, pady=10)
        Label(self.lateral, text='A', background='#414141', foreground='white').grid(row=1, column=1, sticky='w', padx=0, pady=10)
        Label(self.lateral, text='Ingrese la tensión del banco de baterías', background='#414141', foreground='white').grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)
        self.text3 = Text(self.lateral, height=1, width=10)
        self.text3.grid(row=3, column=0, sticky='e', padx=4, pady=10)
        Label(self.lateral, text='V', background='#414141', foreground='white').grid(row=3, column=1, sticky='w', padx=0, pady=10)
        Label(self.lateral, text='Capacidad del Banco:', background='#414141', foreground='white').grid(row=4, column=0, sticky='w',columnspan=2, padx=10, pady=10 )
        style = ttk.Style()
        style.configure("TScale.Horizontal.TScale", background="white")
        
        self.banco = ttk.Scale(self.lateral, from_=45, to=200, orient="horizontal", command=self.Tomavalor, style="TScale.Horizontal.TScale")
        self.banco.grid(row=5, column=0, sticky='e', padx=4, pady=10)
        self.valt=Label(self.lateral, text='45 AH', background='#414141', foreground='white')
        self.valt.grid(row=5, column=1, sticky='w')

        Label(self.gif, text='Resultados:', background='#414141', foreground='white').grid(row=7, column=0, sticky='w', padx=0, pady=10)
        
        self.potencia=Label(self.gif, text='Potencia', background='#414141', foreground='white')
        self.potencia.grid(row=8, column=0, sticky='w',columnspan=2, padx=10, pady=10 )

        self.autonmiaideal=Label(self.lateral, text='Autonomía Ideal', background='#414141', foreground='white')
        self.autonmiaideal.grid(row=9, column=0, sticky='w',columnspan=2, padx=10, pady=10 )

        self.autonomíaporcentual=Label(self.lateral, text='Autonomía Porcentual', background='#414141', foreground='white')
        self.autonomíaporcentual.grid(row=10, column=0, sticky='w',columnspan=2, padx=10, pady=10 )

        self.gif_canvas = Canvas(self.gif, bg='#414141', width=250, height=250)
        self.gif_canvas.grid(row=0, column=0, padx=10, pady=10, columnspan=2)




    

    def create_buttons(self):
        style = ttk.Style()        
        style.configure("Fancy.TButton", foreground="white", background="#0099ff", borderwidth=0) 
        #Button del convertidor de máscara       
        self.btn1 = ttk.Button(self.mascfr, text="Convertir", command=self.mascaraRed, style='Fancy.TButton')
        self.btn1.grid(row=5,column=2, pady=10)
        #Button del convertidor de IButtons
        self.btn2 = ttk.Button(self.ibut, text='Convertir',command=self.convertibut, style='Fancy.TButton')
        self.btn2.grid(row=4, column=1, padx=10, pady=10)
        #Button de potencia
        self.btn3 = ttk.Button(self.lateral, text='Calcular',command=self.CalcPotencia, style='Fancy.TButton')
        self.btn3.grid(row=6, column=0, sticky='e', padx=10, pady=10)
         #Button de gif
        self.btn4 = ttk.Button(self.gif, text='gif',command=self.load_and_display_gif, style='Fancy.TButton')
        self.btn4.grid(row=2, column=0, sticky='e', padx=10, pady=10)

    def load_and_display_gif(self):
        # Ruta al archivo GIF
        gif_path = "like.gif"

        # Carga el GIF como una secuencia de imágenes
        gif_frames = imageio.get_reader(gif_path)

        # Recorre todas las imágenes y las muestra en el Canvas
        for i, frame in enumerate(gif_frames):
            # Convierte el array de píxeles a una imagen de PIL
            image = Image.fromarray(frame)
            image = image.resize((150, 150))  # Ajusta el tamaño según tus necesidades

            # Convierte la imagen a un formato compatible con Tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Configura la imagen en el Canvas
            self.gif_canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
            self.gif_canvas.image = tk_image

            # Actualiza la interfaz gráfica para mostrar el siguiente frame
            self.root.update_idletasks()

            # Espera un breve periodo para lograr la animación
            self.root.after(100)  # Ajusta el tiempo de espera según sea necesario


    def CalcPotencia(self):
        print('potencia')
        I = int(self.text2.get("1.0", "end-1c"))
        V = int(self.text3.get("1.0", "end-1c"))
        P = round(I * V * 0.8, 2)  # se redondea al segundo decimal round(numero, 2)
        print('Potencia:', P)
        self.potencia.config(text=f'Potencia: {P} W')
        Cap = self.banco.get()

        Cap = float(Cap)
        Cap = round(Cap)
        Autonomia = round(Cap / I, 2)
        AutReal = round(Autonomia * 0.8, 2)
        self.autonmiaideal.config(text=f'Autonmía ideal = {Autonomia} h')
        self.autonomíaporcentual.config(text=f'Autonomía porcentual(80%) = {AutReal} h')
        self.load_and_display_gif()


    def Tomavalor(self, valor):
        
        print(valor)
        valor=float(valor)
        valor=round(valor)
        self.valt.config(text=f'{valor} AH')

    def mascaraRed(self):
        x = self.texto.get("1.0", "end-1c")
        x = x.strip("\n")

        try:
            x = int(x)
        except ValueError:
            self.mascara = "Ingrese un valor numérico válido"
            self.resulmasc.delete("1.0", "end")
            self.resulmasc.insert("1.0", self.mascara)
            return

        print(x)

        if 0 <= x < 33:
            print('x:', x)

            # Calcula los octetos completos y los bits adicionales
            octetos_completos = x // 8
            bits_adicionales = x % 8

            # Construye la máscara de red
            self.mascara = [255] * octetos_completos

            if bits_adicionales > 0:
                valor_bits_adicionales = 2 ** (8 - bits_adicionales) - 1
                self.mascara.append(valor_bits_adicionales)

            # Completa la máscara de red con ceros
            while len(self.mascara) < 4:
                self.mascara.append(0)

            self.resulmasc.delete("1.0", "end")
            self.resulmasc.insert("1.0", ".".join(map(str, self.mascara)))

            return ".".join(map(str, self.mascara))
        else:
            self.mascara = "El valor de la máscara debe estar entre 0 y 32"
            self.resulmasc.delete("1.0", "end")
            self.resulmasc.insert("1.0", self.mascara)
    
    def convertibut(self):
        print('hola')
        result=self.texto2.get(1.0, tk.END+"-1c")
        self.letra = []
        self.par=[]
        i=0
        for x in result:
            self.letra.append(x)
            y = str(self.letra[i-1]) + str(self.letra[i])
            if i%2 != 0:
                self.par.append(y)
            i=i+1
        inver = self.par[::-1]
        
        salida = ''.join(inver)
        
        self.resulibut.delete("1.0", "end")
        self.resulibut.insert("1.0", salida)
    
    


    











if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = calculadoraRED(root)
    root.mainloop()





