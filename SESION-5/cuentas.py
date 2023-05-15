class Cuenta:
    def __init__(self, _titular, _saldo):
        self.titular = _titular
        self.saldo = _saldo

class Plazo_fijo(Cuenta):
    def __init__(self, _titular, _saldo):
        super().__init__(_titular, _saldo)

class Caja_ahorro(Cuenta):
    def __init__(self, _titular, _saldo, _plazo, _interes):
        super().__init__(_titular, _saldo)
        self.plazo = _plazo
        self.interes = _interes

