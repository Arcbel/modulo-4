class Alumno:
    semestre = 1
    asignatura = ['Python', 'Javascript', 'Base de datos']
    

    def __init__(self, _name):
        self.name = _name
        self.notas = []

    def inscribir_asignatura(self, _asignatura):
        if _asignatura in self.asignatura:
            print(f'{self.name} ha inscrito la asignatura: {_asignatura}')
        else:
            print('Esta asignatura no existe.')

    def registrar_nota(self, _nota_1):
        self.notas.append(_nota_1)

    def promedio_notas(self):
        promedio = sum(self.notas) / len(self.notas)
        print(f'El promedio de notas de {self.name} es: {promedio}')


alumno1 = Alumno('Franco')
alumno2 = Alumno('Daniel')
alumno3 = Alumno('Tamara')

print(f'Alumno 1: {alumno1.name} --- Alumno 2: {alumno2.name} --- Alumno 3: {alumno3.name}')
print(f'Semestre almuno 1: {alumno1.semestre} --- Semestre almuno 2: {alumno2.semestre} --- Semestre almuno 3: {alumno3.semestre}')

alumno2.semestre = 2
print(f'Semestre almuno 1: {alumno1.semestre} --- Semestre almuno 2: {alumno2.semestre} --- Semestre almuno 3: {alumno3.semestre}')

Alumno.semestre = 4
print(f'Semestre almuno 1: {alumno1.semestre} --- Semestre almuno 2: {alumno2.semestre} --- Semestre almuno 3: {alumno3.semestre}')

alumno1.inscribir_asignatura('Base de datos')
alumno1.registrar_nota(7)
alumno1.registrar_nota(4)
alumno1.registrar_nota(3)
alumno1.promedio_notas()

alumno2.inscribir_asignatura('Python')
alumno2.registrar_nota(7)
alumno2.registrar_nota(5)
alumno2.registrar_nota(6.5)
alumno2.promedio_notas()