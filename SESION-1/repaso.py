requisitos = {
    'Título': 'requerido',
    'Notas': 'requerido',
    'Foto': 'opcional'
}

print(requisitos)

#Acceder a una propiedad
print(f'Las notas son de tipo: {requisitos["Notas"]}')
print(f'La foto es de tipo: {requisitos["Foto"]}')

#Modificar una propiedad
requisitos['Foto'] = 'requerido'
print(f'La foto es de tipo: {requisitos["Foto"]}')

#Practica: Contruir un diccionario de datos para guardar
#           la iinformacion de un avion, coloque al menos 6 propiedades
#           imprima 3 de llas y cambie el valor de los
#           al menos debe existir una prop booleana, una entera, una flotante
#           un arreglo, un diccionario, un string

avion = {
    'linea': 'LAN',
    'capacidad_pasajeros': 250,
    'operativo': True,
    'Tripulantes': {
        'Piloto': 'John Smith',
        'Copiloto': 'Juanita Parra',
        'Azafata': 'Silvia Rodriguez'
    },
    'asientos': ['economic', 'turist', 'executiv'],
    'capacidad_carga': 1.7
}

#Practica: Construya un programa que solicite el peso en kg de una persona
# y si el peso está entre 60 y 70 recomiende una dieta de 5 comidas altas en carbohidratos
#si el peso está entre 71 y 80 recomiende una dieta de 4 comidas altas en proteína
#si es peso es mayor a 80 recomiende una dieta de 3 comidas altas en fibra
#utilice solo diccionarios para agrupar los respectivos menues

peso = float(input('Ingrese su peso: '))

if 60 <= peso <= 70:
    dieta_alta_carbohidrato = {
        'desayuno': 'Batido de frutas, con yogurt, granola y avena',
        'media_mañana': 'chocolate',
        'almuerzo': 'arroz con porotos negos',
        'media_tarde': 'panqueques de avena',
        'cena': 'fideos con salsa'
    }
    print(f'Debe seguir la siguiente dieta alta en carbohidratos: {dieta_alta_carbohidrato}')
elif 70 < peso <= 80:
    dieta_alta_proteina = {
        'desayuno': 'batido de proteina y una mitad de pechuga de pollo',
        'media_mañana': 'almendras',
        'almuerzo': 'pechuga completa de pollo, con tortilla de verduras',
        'cena': 'panqueques salados de proteina con pollo y un poquito de crema',
    }
    print(f'Debe seguir la siguiente dieta alta en proteína: {dieta_alta_proteina}')
elif peso > 80:
    dieta_alta_fibra ={
        'desayuno': 'cereal con frutas y leche de soja',
        'almuerzo': 'garbanzos con arroz integral y brocoli',
        'cena': 'pan integral con mermelada sin azucar'
    }
    print(f'Debe seguir la siguiente dieta alta en fibra: {dieta_alta_fibra}')