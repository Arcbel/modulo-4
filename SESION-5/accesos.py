class Empleado:
    sueldo = 0

    def __init__(self, _name):
        self.name = _name

persona1 = Empleado('Juan Perez')
print(persona1.name)

class Empleadoprotected:
    sueldo = 0

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,_name):
        self.__name = _name

persona2 = Empleadoprotected('maria')
print(persona2.name)

persona2.name = 'Juan'
print(persona2.name)