def aplicarAumento(precio:float):
    valor_final = precio + (precio * 0.05)
    return valor_final

precio_con_aumento = aplicarAumento(float(input("Ingrese monto: ")))
print(precio_con_aumento)