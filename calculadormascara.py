def calcular_mascara_red(x):
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
    
    return ".".join(map(str, mascara))


# Solicita al usuario ingresar el valor "/x"
valor_x = int(input("Ingrese el valor '/x' para la máscara de red: "))

# Calcula y muestra la máscara de red correspondiente
mascara_red = calcular_mascara_red(valor_x)
print("La máscara de red correspondiente es:", mascara_red)
