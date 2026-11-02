Repositorio_pacientes = []
Tamanio_maximo = 5

while len(Repositorio_pacientes) < Tamanio_maximo:
    print(f"\nPaciente {len(Repositorio_pacientes) + 1} de {Tamanio_maximo}")

    nombre = input("Nombre completo: ").lower()

    edad = 0
    edad_valida = False
    
    while not edad_valida:
        try:
            edad = int(input("Edad: "))
            if edad >= 3:
                edad_valida = True
            else:
                print("La edad debe ser mayor o igual a 3")
        except ValueError:
            print("Ingrese un numero entero")
            
    Repositorio_pacientes.append({"nombre": nombre, "edad": edad})

print("\nRepositorio completo de pacientes:")
print(Repositorio_pacientes)

with open("pacientes_cremacion.txt", "w", encoding="utf-8") as archivo_pacientes:
    archivo_pacientes.write("REPOSITORIO DE PACIENTES A CREMAR\n")
    archivo_pacientes.write("=" * 50 + "\n")
    for i, paciente in enumerate(Repositorio_pacientes, 1):
        archivo_pacientes.write(f"{i}. Nombre: {paciente['nombre'].title()} | Edad: {paciente['edad']} años\n")
    archivo_pacientes.write("=" * 50 + "\n")
    archivo_pacientes.write(f"Total de pacientes registrados: {len(Repositorio_pacientes)}\n")

print("¡Guardado en pacientes_cremacion.txt!")

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
    print("=" * 50)
    print("INVENTARIO COMPLETO DE INSUMOS: ")
    print("-" * 50)
    for i, insumo in enumerate(lista_insumos, 1):
        print(f"{i}. {insumo['Nombre']} - Cantidad: {insumo['Cantidad']}")
    print(f"\nTotal de insumos registrados: {len(lista_insumos)}")
    print("=" * 50)

with open("inventario_cremacion.txt", "w", encoding="utf-8") as archivo_insumos:
    archivo_insumos.write("INVENTARIO DE INSUMOS PARA CREMACION\n")
    archivo_insumos.write("=" * 50 + "\n")
    for i, insumo in enumerate(lista_insumos, 1):
        archivo_insumos.write(f"{i}. {insumo['Nombre']} - Cantidad: {insumo['Cantidad']}\n")
    archivo_insumos.write("=" * 50 + "\n")
    archivo_insumos.write(f"Total de insumos registrados: {len(lista_insumos)}\n")

print("\n¡Guardado en inventario_cremacion.txt!")
