from Objeto import Objeto

class Telefono(Objeto):
    def __init__(self, name: str, price: float, quantity=0,broken_phones=0):
        super().__init__(name, price, quantity)
        #Arguments validation
        assert broken_phones >= 0, "Broken phones must be equal or greater than 0"
        assert broken_phones <= quantity, "The amount of broken phones can't be greater that the total amount of phones"

        #Arguments asiggnment
        self.broken_phones = broken_phones