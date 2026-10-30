lista_insumos = []
Cantidad_maxima_insumos = 15

print("\n\n===== REGISTRO DE INSUMOS PARA CREMACION =====")
print(f"Puede registrar hasta {Cantidad_maxima_insumos} insumos. \n")

while len(lista_insumos) < Cantidad_maxima_insumos: 
    print(f"--- Insumo {len(lista_insumos) + 1} de {Cantidad_maxima_insumos} ---")

    nombre_insumo = input("Nombre del insumo: ").strip()

    try:
        Cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("La cantidad debe ser un numero entero. Intentalo de nuevo.")
        continue
    lista_insumos.append({"Nombre": nombre_insumo, "Cantidad": Cantidad})
    print(f"Insumo registrado\n")
    print("="*50)
    print("INVENTARIO COMPLETO DE INSUMOS: ")
    print("-"*50)
    for i, insumo in enumerate(lista_insumos, 1):
        print(f"{i}. {insumo['Nombre']} - Cantidad: {insumo['Cantidad']}")
        print(f"\nTotal de insumos registrados: {len(lista_insumos)}")
        print("="*50)

with open("inventario_cremacion.txt", "w", encoding="utf-8") as archivo:
    archivo.write("INVENTARIO DE INSUMOS PARA CREMACION\n")
    archivo.write("="*50 + "\n")
    for i, insumo in enumerate(lista_insumos, 1):
        archivo.write(f"{i}. {insumo['Nombre']} - Cantidad: {insumo['Cantidad']}\n")
    archivo.write("="*50 + "\n")
    archivo.write(f"Total de insumos registrados: {len(lista_insumos)}\n")

print("\n¡Guardado en inventario_cremacion.txt!")

