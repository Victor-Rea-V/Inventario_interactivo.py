


lista = [ {"Nombre_finca": "La Libertad", "Ubicación": "Santa Elena", "Hectareas": 16.8},
             {"Nombre_finca": "Macas", "Ubicación": "La Maná", "Hectareas": 20.5},
             {"Nombre_finca": "Arena", "Ubicación": "Guayas", "Hectareas": 35.3}] 

# Función para agregar una nueva finca a la lista

def agregar_finca(lista_fincas):
    
    # Cantidad de fincas
    print(f"Cantidad de fincas antes actuales: {len(lista)}")

# Pides los nuevos valores
    print("Ingreso de nueva Finca:")
    Nombre_finca = input("Ingresa el nombre de la nueva finca de cacao: ")
    Ubicación = input("Ingresa la ubicación: ")
    Hectareas= float(input("Ingresa el número de hectáreas: "))


# nueva lista
    nueva_finca={ "Nombre":Nombre_finca,"Ubicación":Ubicación,"Hectareas":Hectareas}

# .append() agrega el nuevo diccionario al final de nuestra lista
    lista_fincas.append(nueva_finca)
    print(f"¡Éxito! La finca '{Nombre_finca}' ha sido registrada correctamente.\n")
    print(f"Cantidad de fincas acatualmente son : {len(lista_fincas)}")
    print(f"La última finca agregada es: {lista[-1]}")

# Llamamos a la función para agregar una nueva finca
agregar_finca(lista)