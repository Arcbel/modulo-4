class Persona:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

class Maestro(Persona):
    def __init__(self, _name, _age, _profession):
        super().__init__(_name, _age)
        self.profession = _profession

class Estudiante(Persona):
    def __init__(self, _name, _age, _interest):
        super().__init__(_name, _age)
        self.interest = _interest
    
class Universitario(Estudiante):
    def __init__(self, _name, _age, _interest, _university):
        super().__init__(_name, _age, _interest)
        self.university = _university


