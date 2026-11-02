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
            if edad >=3:
                edad_valida = True
            else:
                print("La edad debe ser mayor o igual a 3")
        except:
            print("Ingrese un numero entero")
    Repositorio_pacientes.append({"nombre": nombre, "edad": edad})
print("\nRepositorio completo")
print(Repositorio_pacientes)

