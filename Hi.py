class objeto:
    discount_porcentage = .9
    instaces = []
    def __init__(self, name: str, price: float, quantity=0):
        #Arguments validations
        assert price >= 0,"Price must be equal or greater than 0"
        assert quantity >= 0, "Quantity must be equal or greater than 0"

        #Arguments asiggnment
        self.name = name
        self.price = price
        self.quantity = quantity

        # Extra actions 
        objeto.instaces.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price = self.price * self.discount_porcentage
    
    def __repr__(self):
        return f"Objeto(name= '{self.name}', price= '{self.price}', quantity= '{self.quantity}')"

objeto1 = objeto(name= "Iphone", price= 10000, quantity= 25)
objeto2 = objeto(name= "Headset", price= 5000, quantity= 49)
objeto3 = objeto(name= "Violin", price= 600, quantity= 32)
objeto4 = objeto(name= "Mouse", price= 4000, quantity= 17)
objeto5 = objeto(name= "Apple", price= 50, quantity= 7)

print(objeto.instaces)