from tkinter import *
import tkinter as tk





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
    

    


#creamos la ventana del programa
root = tk.Tk()
root.geometry("400x240")
root.title("Calcular máscara")



#creamos la variable entrada y la poscionamos

textExample=tk.Text(root, height=1, width=15)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Calcular", command=calcular_mascara_red)


btnRead.pack()

respuesta = tk.Entry(root)
respuesta.pack()



root.mainloop()




