class Padre:
    
    def __init__(self, _name, _rut_padre):
        self.name = _name
        self.rut = _rut_padre
        self.sueldo = 0
    def pintar(self, _color):
        print(f'{self.name} esta pintando con {_color}')
        


class Hijo(Padre):
    def __init__(self, _name_hijo, _rut_hijo, _color_ojos):
        Padre.__init__(self, _name_hijo, _rut_hijo)
        self.color_ojos = _color_ojos

        


richar = Padre('Richar Lujano', '11.111.111-1')
richard = Hijo('Richard Lujano', '22.222.222-2', 'Marron')

print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo)

richar.pintar('morado')
print(richard.pintar)

richard.pintar('gris')
print(richard.pintar)
