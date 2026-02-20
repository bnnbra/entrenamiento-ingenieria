def calcular_nomina(sueldo_bruto):
    if sueldo_bruto <= 0:
        return "Error: Sueldo no válido"
    
    impuestos = sueldo_bruto * 0.15
    sueldo_neto = sueldo_bruto - impuestos
    return sueldo_neto

# Prueba profesional
mi_sueldo = 2500
print(f"Sueldo tras impuestos: {calcular_nomina(mi_sueldo)}")
