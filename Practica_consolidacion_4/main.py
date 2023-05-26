import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'vehiculo.csv')

class Vehiculo:
    def __init__(self, _marca, _modelo, _num_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"
    
    def registro_vehiculos():
        num_vehiculos = 0
        while True:
            try:
                num_vehiculos = int(input('Cuantos vehículos desea insertar: '))
                break  
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        lista_vehiculos = []

        for i in range(num_vehiculos):
            print(f"Datos del automóvil {i + 1}")

            while True:
                marca = input("Inserte la marca del automóvil: ")
                if marca:
                    break

                print("Error: La marca no puede estar vacía.")

            while True:
                modelo = input("Inserte el modelo: ")
                if modelo:
                    break

                print("Error: El modelo no puede estar vacío.")

            while True:
                try:
                    ruedas = int(input("Inserte el número de ruedas: "))
                    if ruedas > 0:
                        break

                    print("Error: El número de ruedas debe ser mayor a cero.")
                except ValueError:
                    print("Error: Debe ingresar un número válido para las ruedas.")

            while True:
                try:
                    velocidad = int(input("Inserte la velocidad en km/h: "))
                    if velocidad > 0:
                        break

                    print("Error: La velocidad debe ser mayor a cero.")
                except ValueError:
                    print("Error: Debe ingresar un número válido para la velocidad.")

            while True:
                try:
                    cilindrada = int(input("Inserte el cilindraje en cc: "))
                    if cilindrada > 0:
                        break

                    print("Error: El cilindraje debe ser mayor a cero.")
                except ValueError:
                    print("Error: Debe ingresar un número válido para el cilindraje.")

            automovil = Automovil(marca, modelo, ruedas, velocidad, cilindrada)
            lista_vehiculos.append(automovil)

        print("\nImprimiendo por pantalla los vehículos:")
        for vehiculo in lista_vehiculos:
            print(vehiculo)

    def guardar_datos_csv(self):
        tipo_vehiculo = type(self).__name__
        datos = str(self.__dict__)

        if not os.path.isfile(csv_path):
            with open(csv_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tipo_vehiculo, datos])
        else:
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == tipo_vehiculo and row[1] == datos:
                        return

            with open(csv_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tipo_vehiculo, datos])

    def leer_datos_csv():
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            vehiculos = {}

            for row in reader:
                tipo_vehiculo = row[0]
                datos = eval(row[1])

                if tipo_vehiculo == 'Particular':
                    vehiculo = Particular(*datos.values())
                elif tipo_vehiculo == 'Carga':
                    vehiculo = Carga(*datos.values())
                elif tipo_vehiculo == 'Bicicleta':
                    vehiculo = Bicicleta(*datos.values())
                elif tipo_vehiculo == 'Motocicleta':
                    vehiculo = Motocicleta(*datos.values())
                else:
                    continue

                if tipo_vehiculo in vehiculos:
                    vehiculos[tipo_vehiculo].append(vehiculo)
                else:
                    vehiculos[tipo_vehiculo] = [vehiculo]

        for tipo, lista in vehiculos.items():
            print(f"Lista de Vehículos {tipo}:")
            for vehiculo in lista:
                print(vehiculo.__dict__)
            print()

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _num_ruedas)
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"
    
class Particular(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _num_puestos):
        super().__init__(_marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.num_puestos = _num_puestos

    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.num_puestos}"

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _peso_carga):
        super().__init__(_marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.peso_carga}"

class Bicicleta (Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta):
        super().__init__(_marca, _modelo, _num_ruedas)
        self.tipo_bicicleta = _tipo_bicicleta

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo_bicicleta}"

class Motocicleta (Bicicleta):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta, _motor, _cuadro,  _num_radios):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_bicicleta)
        self.cuadro = _cuadro
        self.num_radios = _num_radios
        self.motor = _motor

    def __str__(self):
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro. radios: {self.num_radios}"

# Parte 1
Vehiculo.registro_vehiculos()

# Parte 2
print("_______________________________________________________")
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)


print("\nVerificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular, Carga, Bicicleta y Motocicleta.")
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

#Parte 3
print("_______________________________________________________")
particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

Vehiculo.leer_datos_csv()
